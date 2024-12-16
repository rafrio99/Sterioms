from django.http import HttpRequest
from rest_framework.exceptions import AuthenticationFailed
from core.serializers import (
    HealthFacility,
    HealthFacilitySerializer,
    Department,
    DepartmentSerializer,
    Employee,
    EmployeeStatus,
    EquipmentCategory,
    Equipment,
    SterilizationMethod,
    Batch,
    BatchEquipment,
    Stage,
    OperationLog,
    Package,
    PackageItem,
    StorageRecord,
    DistributionRecord,
    LoginCode,
    LoginTable,
)
from django.core.exceptions import ValidationError
from core.serializers import (
    HealthFacility,
    HealthFacilitySerializer,
    EmployeeStatusSerializer,
    EmployeeSerializer,
    EquipmentCategorySerializer,
    EquipmentSerializer,
    SterilizationMethodSerializer,
    BatchSerializer,
    BatchEquipmentSerializer,
    StageSerializer,
    OperationLogSerializer,
    PackageSerializer,
    PackageItemSerializer,
    StorageRecordSerializer,
    DistributionRecordSerializer,
)


# Health_facility
def get_facilities():
    return HealthFacility.objects.all()


def get_facility_by_id(id: str | None = None):
    try:
        facility = HealthFacility.objects.get(pk=id)
    except (HealthFacility.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return facility


def facility_info(facility: HealthFacility, many: bool = False):
    return HealthFacilitySerializer(facility, many=many).data


# Department
def get_departments():
    return Department.objects.all()


def get_department_by_id(id: str | None = None):
    try:
        department = Department.objects.get(pk=id)
    except (Department.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return department


def get_departments_by_facility(facility: HealthFacility):
    return Department.objects.filter(health_facility=facility)


def department_info(department: Department, many: bool = False):
    return DepartmentSerializer(department, many=many).data


# Employee Status
def get_employee_statuses():
    return EmployeeStatus.objects.all()


def get_employee_status_by_id(id: str | None = None):
    try:
        status = EmployeeStatus.objects.get(pk=id)
    except (EmployeeStatus.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return status


def employee_status_info(emp_status: EmployeeStatus, many: bool = False):
    return EmployeeStatusSerializer(emp_status, many=many).data


# Employees
def get_employees():
    return Employee.objects.all()


def get_employee_by_id(id: str | None = None):
    try:
        status = Employee.objects.get(pk=id)
    except (Employee.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return status


def get_employees_by_facility(facility: HealthFacility):
    return Employee.objects.filter(department__health_facility=facility)


def employee_info(employee: Employee, many: bool = False):
    return EmployeeSerializer(employee, many=many).data


# Equipment Category
def get_equipment_categories():
    return EquipmentCategory.objects.all()


def get_equipment_category_by_id(id: str | None = None):
    try:
        equipment = EquipmentCategory.objects.get(pk=id)
    except (EquipmentCategory.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return equipment


def equipment_category_info(category: EquipmentCategory, request: HttpRequest):
    data = EquipmentCategorySerializer(category).data
    return data


def equipment_category_info_mul(
    categories: list[EquipmentCategory], request: HttpRequest
):
    return [equipment_category_info(category, request) for category in categories]


# Equipment
def get_equipments():
    return Equipment.objects.all()


def get_equipment_by_id(id: str | None = None):
    try:
        status = Equipment.objects.get(pk=id)
    except (Equipment.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return status


def equipment_info(equipment: Equipment, request: HttpRequest):
    data = EquipmentSerializer(equipment).data
    data["category"] = (
        equipment_category_info(equipment.category, request)
        if equipment.category
        else None
    )
    return data


def equipment_info_mul(equipment: list[Equipment], request: HttpRequest):
    return [equipment_info(eq, request) for eq in equipment]


# Sterilization Method
def get_sterilization_methods():
    return SterilizationMethod.objects.all()


def get_sterilization_method_by_id(id: str | None = None):
    try:
        sm = SterilizationMethod.objects.get(pk=id)
    except (SterilizationMethod.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return sm


def sterilization_method_info(method: SterilizationMethod, request: HttpRequest):
    data = SterilizationMethodSerializer(method).data
    return data


def sterilization_method_info_mul(
    methods: list[SterilizationMethod], request: HttpRequest
):
    return [sterilization_method_info(sm, request) for sm in methods]


# Batch
def get_batches(facility: HealthFacility | None = None):
    batches = Batch.objects.all()
    if facility:
        batches = batches.filter(operator__department__health_facility=facility)
    return batches


def get_batch_by_id(id: str | None = None):
    try:
        batch = Batch.objects.get(pk=id)
    except (Batch.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return batch


def batch_packaged(batch):
    """Check if a batch is already packaged before you attempt packaging again"""
    return PackageItem.objects.filter(batch=batch).exists()


def batch_sterilized():
    pass


def batch_info(batch: Batch, many: bool = False):
    return BatchSerializer(batch, many=many).data


# Batch Equipment
def get_batch_equipments():
    return BatchEquipment.objects.all()


def get_batch_equipment_by_id(id: str | None = None):
    try:
        beq = BatchEquipment.objects.get(pk=id)
    except (BatchEquipment.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return beq


def batch_equipment_info(batch_equipment: BatchEquipment, many: bool = False):
    return BatchEquipmentSerializer(batch_equipment, many=many).data


# Stage
def get_stages():
    return Stage.objects.all()


def get_stage_by_id(id: str):
    try:
        stage = Stage.objects.get(pk=id)
    except (Stage.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return stage


def get_stage_by_rank(rank: int | None = None):
    try:
        stage = Stage.objects.get(stage_number=rank)
    except (Stage.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return stage


def stage_info(stage: Stage, many: bool = False):
    return StageSerializer(stage, many=many).data


# OperationLog
def get_operation_logs():
    return OperationLog.objects.all()


def get_operation_log_by_id(id: str | None = None):
    try:
        status = OperationLog.objects.get(pk=id)
    except (OperationLog.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return status


def operation_log_info(operation_log: OperationLog, many: bool = False):
    return OperationLogSerializer(operation_log, many=many).data


# Package
def get_packages(facility: HealthFacility | None = None):
    packages = Package.objects.all()
    if facility:
        packages = packages.filter(operator__department__health_facility=facility)
    return packages


def get_package_by_id(id: str | None = None):
    try:
        package = Package.objects.get(pk=id)
    except (Package.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return package


def package_info(package: Package, many: bool = False):
    return PackageSerializer(package, many=many).data


# PackageItem
def get_package_items():
    return PackageItem.objects.all()


def get_package_item_by_id(id: str | None = None):
    try:
        pitem = PackageItem.objects.get(pk=id)
    except (PackageItem.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return pitem


def package_item_info(package_item: PackageItem, many: bool = False):
    return PackageItemSerializer(package_item, many=many).data


# Storage Records
def get_storage_records(facility: HealthFacility | None = None):
    records = StorageRecord.objects.all()
    if facility:
        records = records.filter(
            package__operator__department__health_facility=facility
        )
    return records


def get_storage_record_by_id(id: str | None = None):
    try:
        st_record = StorageRecord.objects.get(pk=id)
    except (StorageRecord.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return st_record


def package_in_storage(package: Package):
    return StorageRecord.objects.filter(package=package).exists()


def storage_record_info(storage_record: StorageRecord, many: bool = False):
    return StorageRecordSerializer(storage_record, many=many).data


# Distribution Record
def get_distribution_records(facility: HealthFacility | None = None):
    records = DistributionRecord.objects.all()
    if facility:
        records = records.filter(operator__department__health_facility=facility)
    return records


def package_distributed(package: Package):
    return DistributionRecord.objects.filter(package=package).exists()


def get_distribution_record_by_id(id: str | None = None):
    try:
        ds_record = DistributionRecord.objects.get(pk=id)
    except (DistributionRecord.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return ds_record


def distribution_record_info(dist_record: DistributionRecord, many: bool = False):
    return DistributionRecordSerializer(dist_record, many=many).data


def get_login_code(employee: Employee):
    try:
        code = LoginCode.objects.get(employee=employee)
    except (LoginCode.DoesNotExist, ValidationError, ValueError):
        return None
    else:
        return code


def get_token_frm_header(request: HttpRequest):
    access_token = request.headers.get("Access-Token")
    if not access_token:
        context = {
            "detail": "Authentication failed",
            "status": "failed",
            "errors": "Access-Token header is required but not set",
        }
        raise AuthenticationFailed(context)
    id_token = access_token.split("+")
    if len(id_token) < 2:
        context = {
            "detail": "Authentication failed",
            "status": "failed",
            "errors": "You provided an invalid token",
        }
        raise AuthenticationFailed(context)

    return tuple(id_token)


def authenticated(request: HttpRequest):

    employee, token = get_token_frm_header(request)
    try:
        login_info = LoginTable.objects.get(employee=employee, token=token)
    except LoginTable.DoesNotExist:
        context = {
            "detail": "Authentication failed",
            "status": "failed",
            "errors": "Invalid authentication credentials. You are not logged in.",
        }
        raise AuthenticationFailed(context)
    else:
        return login_info
