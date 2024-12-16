from core.serializers import (
    HealthFacilitySerializer,
    DepartmentSerializer,
    EmployeeSerializer,
    EmployeeStatusSerializer,
    EquipmentSerializer,
    EquipmentCategorySerializer,
    SterilizationMethodSerializer,
    BatchSerializer,
    BatchEquipmentSerializer,
    StageSerializer,
    OperationLogSerializer,
    PackageSerializer,
    PackageItemSerializer,
    StorageRecordSerializer,
    DistributionRecordSerializer,
    LoginCodeSerializer,
    LoginTableSerializer,
)


# Health Facility
def create_hfacility(data, **kwargs):
    serializer = HealthFacilitySerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def update_hfacility(data, instance, **kwargs):
    serializer = HealthFacilitySerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Department
def create_department(data, **kwargs):
    serializer = DepartmentSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def update_department(data, instance, **kwargs):
    serializer = DepartmentSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Employee Status
def create_employee_status(data, **kwargs):
    serializer = EmployeeStatusSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def update_employee_status(data, instance, **kwargs):
    serializer = EmployeeStatusSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Employee
def create_employee(data, **kwargs):
    serializer = EmployeeSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def update_employee(data, instance, **kwargs):
    serializer = EmployeeSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Equipment Category
def create_equipment_category(data, **kwargs):
    serializer = EquipmentCategorySerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_equipment_category(data, instance, **kwargs):
    serializer = EquipmentCategorySerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Equipment
def create_equipment(data, **kwargs):
    serializer = EquipmentSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_equipment(data, instance, **kwargs):
    serializer = EquipmentSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Sterilization Methods
def create_sterilization_method(data, **kwargs):
    serializer = SterilizationMethodSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_sterilization_method(data, instance, **kwargs):
    serializer = SterilizationMethodSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Batch
def create_batch(data, **kwargs):
    serializer = BatchSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_batch(data, instance, **kwargs):
    serializer = BatchSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Batch Equipment
def create_batch_equipment(data, **kwargs):
    serializer = BatchEquipmentSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_batch_equipment(data, instance, **kwargs):
    serializer = BatchEquipmentSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Stages
def create_stage(data, **kwargs):
    serializer = StageSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_stage(data, instance, **kwargs):
    serializer = StageSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# OperationLog
def create_operation_log(data, **kwargs):
    serializer = OperationLogSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_operation_log(data, instance, **kwargs):
    serializer = OperationLogSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Package
def create_package(data, **kwargs):
    serializer = PackageSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_package(data, instance, **kwargs):
    serializer = PackageSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Package Item
def create_package_item(data, **kwargs):
    serializer = PackageItemSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_package_item(data, instance, **kwargs):
    serializer = PackageItemSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Storage
def create_storage_record(data, **kwargs):
    serializer = StorageRecordSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_storage_record(data, instance, **kwargs):
    serializer = StorageRecordSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Distribution
def create_distribution_record(data, **kwargs):
    serializer = DistributionRecordSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def modify_distribution_record(data, instance, **kwargs):
    serializer = DistributionRecordSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Login Code
def add_login_code(data, **kwargs):
    serializer = LoginCodeSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


def update_login_code(data, instance, **kwargs):
    serializer = LoginCodeSerializer(
        instance=instance, data=data, partial=True, context=kwargs
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors


# Login Table
def add_login_info(data, **kwargs):
    serializer = LoginTableSerializer(data=data, context=kwargs)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, None
    return None, serializer.errors
