from datetime import datetime
import base64
from random import choice
from string import digits, ascii_letters
from io import BytesIO
from PIL import Image
import barcode
from barcode.writer import ImageWriter
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models import CASCADE, PROTECT, SET_NULL
from phonenumber_field.modelfields import PhoneNumberField

ID_DATE_STR = "%y%m%d"
ID_TIME_STR = "%H%M%S"
DIGITS = digits.replace("0", "")
LETTERS_DIGITS = ascii_letters + digits


DEFAULT_STAGES = [
    {"name": "Collection", "stage_number": 1},
    {"name": "Classification", "stage_number": 2},
    {"name": "Cleaning", "stage_number": 3},
    {"name": "Sterilization", "stage_number": 4},
    {"name": "Packaging", "stage_number": 5},
    {"name": "Storage", "stage_number": 6},
    {"name": "Distribution", "stage_number": 7},
]

DEFAULT_ROLES = [
    {"name": "Administrator", "code": "administrator"},
    {"name": "Facility Director", "code": "facility_director"},
    {"name": "Staff", "code": "staff"},
]


class BarcodeGenerator:
    PREFIX = "data:image/png;base64,"

    def __init__(self) -> None:
        pass

    def generate(self, data):
        buffer = BytesIO()
        writer = ImageWriter()
        options = {
            "module_width": 0.2,
            "module_height": 6,
            "font_size": 8,
            "text_distance": 3.5,
            "write_text": True,
        }
        barcode.get("code128", data, writer=writer).write(buffer, options=options)
        buffer.seek(0)
        return Image.open(buffer)

    def image_file(self, data):
        buffer = BytesIO()
        barcode_image = self.generate(data)
        barcode_image.save(buffer, format="PNG")
        barcode_file = InMemoryUploadedFile(
            buffer, None, f"{data}.png", "image/png", buffer.tell(), None
        )
        return barcode_file

    def enc_im_to_b64(self, data):
        barcode_image = self.generate(data)
        buffer = BytesIO()
        barcode_image.save(buffer, format="PNG")
        buffer.seek(0)
        encoded_string = base64.b64encode(buffer.read()).decode("utf-8")
        return self.PREFIX + encoded_string


class Role(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=20, unique=True)

    @classmethod
    def gen_role_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(3)])
        id = f"ROL{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_role_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_role_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Name: {self.name} | Code: {self.code}"


class HealthFacility(models.Model):
    """This table will store information about the health facilities"""

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=256, unique=True)
    address = models.TextField()
    phone = PhoneNumberField(region=None, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    barcode = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @classmethod
    def gen_facility_id(cls):
        """Automatically generate facility ID"""
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(4)])
        id = f"HF{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_facility_id()
        return id

    def save(self, *args, **kwargs):
        """Give the facility an id when the facility is created"""
        if self._state.adding:
            if not self.id:
                self.id = self.gen_facility_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Facility ID: {self.id}; Name: {self.name}"

    @property
    def departments(self):
        return self.department_set.all()

    @property
    def employees(self):
        return Employee.objects.filter(department__health_facility=self)


class Department(models.Model):
    """This table stores information about departments within each health facility"""

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=256)
    health_facility = models.ForeignKey(to=HealthFacility, on_delete=CASCADE)
    barcode = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Department ID: {self.id}; Name: {self.name}"

    @classmethod
    def gen_department_id(cls):
        """Automatically generate department ID"""
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(4)])
        id = f"HD{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_department_id()
        return id

    def save(self, *args, **kwargs):
        """Give the department an id when the facility is created"""
        if self._state.adding:
            if not self.id:
                self.id = self.gen_department_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)

    @property
    def employees(self):
        return self.employee_set.all()


class EmployeeStatus(models.Model):

    id = models.CharField(primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Status: {self.name}; Code: {self.code}"

    @classmethod
    def gen_employee_status_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(4)])
        id = f"EMS{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_employee_status_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_employee_status_id()
        super().save(*args, **kwargs)


class Employee(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    phone = PhoneNumberField(region=None, null=True, blank=True, unique=True)
    roles = models.ManyToManyField(to=Role, blank=True)
    barcode = models.TextField(null=True, blank=True)
    department = models.ForeignKey(
        to=Department,
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )
    status = models.ForeignKey(
        to=EmployeeStatus,
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Status: {self.name}; ID: {self.pk}"

    @property
    def name(self):
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def role_codes(self):
        return [role.code for role in self.roles.all()]

    def has_role(self, role):
        return self.roles.filter(code=role).exists()

    @classmethod
    def gen_employee_id(cls):
        """Automatically generate employee ID"""
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(6)])
        id = f"{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_employee_id()
        return id

    def save(self, *args, **kwargs):
        """Give the employee an id when the employee is created"""
        if self._state.adding:
            if not self.id:
                self.id = self.gen_employee_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)


class EquipmentCategory(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=256, unique=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self) -> str:
        return f"Status: {self.name}; Code: {self.code}"

    @classmethod
    def gen_equip_category_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(3)])
        id = f"EQC{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_equip_category_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_equip_category_id()
        super().save(*args, **kwargs)


class Equipment(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=256, unique=True)
    code = models.CharField(max_length=20, unique=True)
    barcode = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        to=EquipmentCategory,
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"Name: {self.name}; Category: {self.category.name}"

    @classmethod
    def gen_equipment_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(3)])
        id = f"EQP{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_equipment_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_equipment_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)


class SterilizationMethod(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=256, unique=True)
    barcode = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"ID: {self.pk}; Name: {self.name}; Code: {self.code}"

    @classmethod
    def gen_method_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(4)])
        id = f"SM{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_method_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_method_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)


class Batch(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    sterilization_method = models.ForeignKey(to=SterilizationMethod, on_delete=PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    operator = models.ForeignKey(to=Employee, on_delete=PROTECT)
    completed = models.BooleanField(default=False)
    barcode = models.TextField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"ID: {self.pk}; Created: {self.date_created.date()}; Operator: {self.operator.name}"

    @classmethod
    def gen_batch_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(3)])
        id = f"BAT{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_batch_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_batch_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)

    @property
    def batch_equipment(self):
        equips = self.batchequipment_set.all()
        return equips

    @property
    def logs(self):
        return self.operationlog_set.all()

    def get_log(self, stage):
        # for log in self.logs:
        #     if log.stage_number == stage:
        #         return log
        # return None
        try:
            log = OperationLog.objects.get(batch=self, stage__stage_number=stage)
        except Exception:
            return None
        else:
            return log

    def get_log_geq(self, stage):
        try:
            log = OperationLog.objects.filter(
                batch=self, stage__stage_number__gte=stage
            )
        except Exception:
            return None
        else:
            return log

    @property
    def stages(self):
        stages = [log.stage for log in self.logs]
        return sorted(stages, key=lambda x: x.stage_number)

    @property
    def current_stage(self):
        stages = self.stages
        if not stages:
            return None
        return max(self.stages, key=lambda x: x.stage_number)

    @property
    def sterilized(self):
        return 4 in [int(stage.stage_number) for stage in self.stages]

    @property
    def packed(self):
        return PackageItem.objects.filter(batch=self).exists()

    @property
    def packed_in(self):
        if self.packed:
            return PackageItem.objects.get(batch=self).package
        return None

    @property
    def stored(self):
        if self.packed_in:
            return StorageRecord.objects.filter(package=self.packed_in).exists()
        return False

    @property
    def stored_in(self):
        if self.stored:
            return StorageRecord.objects.get(package=self.packed_in)
        return None


class BatchEquipment(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    batch = models.ForeignKey(to=Batch, on_delete=CASCADE)
    equipment = models.ForeignKey(to=Equipment, on_delete=CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"Name: {self.equipment.name}; Batch: {self.batch.pk}; Quantity: {self.quantity}"

    @classmethod
    def gen_batch_equipment_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(4)])
        id = f"BE{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_batch_equipment_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_batch_equipment_id()
        super().save(*args, **kwargs)


class Stage(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    name = models.CharField(max_length=80)
    stage_number = models.IntegerField(unique=True)
    barcode = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"ID: {self.pk}; Name: {self.name}"

    class Meta:
        ordering = ["stage_number"]

    @classmethod
    def gen_stage_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(3)])
        id = f"STG{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_stage_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_stage_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)


class OperationLog(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    stage = models.ForeignKey(to=Stage, on_delete=CASCADE)
    batch = models.ForeignKey(to=Batch, on_delete=CASCADE)
    operator = models.ForeignKey(to=Employee, on_delete=PROTECT)
    operation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Operation: {self.stage.name}; Batch: {self.batch.pk}"

    @classmethod
    def gen_op_log_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(6)])
        id = f"{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_op_log_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_op_log_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ID: {self.pk} | Stage: {self.stage.name} | Batch: {self.batch.pk}"


class Package(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    operator = models.ForeignKey(to=Employee, on_delete=PROTECT)
    receiver = models.ForeignKey(to=Department, on_delete=PROTECT)
    barcode = models.TextField(null=True, blank=True)
    date_packed = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"ID: {self.pk}; Receiver: {self.receiver.pk}"

    @classmethod
    def gen_pkg_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(3)])
        id = f"PKG{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_pkg_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_pkg_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)

    @property
    def package_items(self):
        items = self.packageitem_set.all()
        return items

    @property
    def batches_in_package(self):
        return [item.batch for item in self.package_items]

    @property
    def stored(self):
        return StorageRecord.objects.filter(package=self).exists()

    @property
    def distributed(self):
        return DistributionRecord.objects.filter(package=self).exists()


class PackageItem(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    package = models.ForeignKey(to=Package, on_delete=CASCADE)
    batch = models.ForeignKey(to=Batch, on_delete=CASCADE)

    def __str__(self) -> str:
        return f"ID: {self.pk} | Package: {self.package.pk}; Batch: {self.batch.pk}"

    @classmethod
    def gen_pkg_item_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(3)])
        id = f"PKI{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_pkg_item_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_pkg_item_id()
        super().save(*args, **kwargs)


class StorageRecord(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)
    package = models.ForeignKey(to=Package, on_delete=CASCADE)
    location = models.CharField(max_length=256)
    storage_number = models.CharField(max_length=50)
    barcode = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Package: {self.package.pk}; Tracker: {self.storage_number}"

    def __str__(self):
        return f"ID: {self.pk} | Package: {self.package.pk}"

    @classmethod
    def gen_storage_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(4)])
        id = f"ST{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_storage_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_storage_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)

    @property
    def distributed(self):
        return self.package.distributed


class DistributionRecord(models.Model):

    id = models.CharField(max_length=20, primary_key=True, unique=True, editable=False)

    package = models.ForeignKey(to=Package, on_delete=CASCADE)
    sent_status = models.BooleanField(default=False)
    date_sent = models.DateTimeField(null=True, blank=True)
    receive_status = models.BooleanField(default=False)
    date_received = models.DateTimeField(null=True, blank=True)
    operator = models.ForeignKey(to=Employee, on_delete=PROTECT)
    barcode = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"Package ID: {self.package.pk}; Receiver: {self.package.receiver.pk}"

    @classmethod
    def gen_distribution_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(6)])
        id = f"{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.gen_distribution_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.gen_distribution_id()
            self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        else:
            if not self.barcode:
                self.barcode = BarcodeGenerator().enc_im_to_b64(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"ID: {self.pk} | Package: {self.package.pk}"


class LoginCode(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=15)
    employee = models.ForeignKey(Employee, on_delete=CASCADE)
    code = models.CharField(max_length=10)
    added = models.TimeField(auto_now=True)

    @classmethod
    def generate_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(6)])
        id = f"{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.generate_id()
        return id

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.generate_id()
        super().save(*args, **kwargs)


class LoginTable(models.Model):
    id = models.CharField(primary_key=True, unique=True, editable=False, max_length=15)
    employee = models.ForeignKey(Employee, on_delete=CASCADE)
    token = models.CharField(max_length=30)
    last_login = models.DateTimeField(auto_now_add=True)

    @classmethod
    def generate_id(cls):
        date_str = datetime.now().date().strftime(ID_DATE_STR)
        s1 = "".join([choice(digits) for i in range(6)])
        id = f"{date_str}{s1}"
        if cls.objects.filter(pk=id):
            cls.generate_id()
        return id

    @classmethod
    def generate_token(cls):
        return "".join([choice(LETTERS_DIGITS) for i in range(25)])

    def save(self, *args, **kwargs):
        if self._state.adding:
            if not self.id:
                self.id = self.generate_id()
            if not self.token:
                self.token = self.generate_token()
        super().save(*args, **kwargs)
