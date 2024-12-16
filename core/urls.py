from django.urls import path
from core.views import (
    HealthFacilityViewset,
    DepartmentViewset,
    EmployeeViewset,
    EmployeeStatusViewset,
    EquipmentCategoryViewset,
    EquipmentViewset,
    SterilizationMethodViewset,
    BatchViewset,
    BatchEquipmentViewset,
    StageViewset,
    OperationLogViewset,
    PackageViewset,
    PackageItemViewset,
    StorageRecordViewset,
    DistributionRecordViewset,
    AuthenticationViewset,
)

app_name = "core"

urlpatterns = [
    # Health Facilities
    path(
        "facilities/",
        HealthFacilityViewset.as_view({"get": "list_facilities"}),
        name="health-facilities",
    ),
    path(
        "facilities/add/",
        HealthFacilityViewset.as_view({"post": "create_facility"}),
        name="create-facility",
    ),
    path(
        "facilities/<str:facility_id>/retrieve/",
        HealthFacilityViewset.as_view({"get": "retrieve_facility"}),
        name="retrieve-facility",
    ),
    path(
        "facilities/<str:facility_id>/departments/",
        HealthFacilityViewset.as_view({"get": "facility_departments"}),
        name="facility-departments",
    ),
    path(
        "facilities/<str:facility_id>/employees/",
        HealthFacilityViewset.as_view({"get": "facility_employees"}),
        name="facility-employees",
    ),
    path(
        "facilities/<str:facility_id>/batches/",
        HealthFacilityViewset.as_view({"get": "facility_batches"}),
        name="facility-batches",
    ),
    path(
        "facilities/<str:facility_id>/packages/",
        HealthFacilityViewset.as_view({"get": "facility_packages"}),
        name="facility-packages",
    ),
    path(
        "facilities/<str:facility_id>/storage-records/",
        HealthFacilityViewset.as_view({"get": "facility_storage_records"}),
        name="facility-storage-records",
    ),
    path(
        "facilities/<str:facility_id>/distribution-records/",
        HealthFacilityViewset.as_view({"get": "facility_distribution_records"}),
        name="facility-distribution-records",
    ),
    path(
        "facilities/<str:facility_id>/update/",
        HealthFacilityViewset.as_view({"put": "update_facility"}),
        name="update-facility",
    ),
    path(
        "facilities/<str:facility_id>/delete/",
        HealthFacilityViewset.as_view({"delete": "delete_facility"}),
        name="update-facility",
    ),
    # Departments
    path(
        "departments/",
        DepartmentViewset.as_view({"get": "list_departments"}),
        name="department",
    ),
    path(
        "departments/add/",
        DepartmentViewset.as_view({"post": "add_department"}),
        name="add-department",
    ),
    path(
        "departments/<str:department_id>/retrieve/",
        DepartmentViewset.as_view({"get": "retrieve_department"}),
        name="retrieve-department",
    ),
    path(
        "departments/<str:department_id>/update/",
        DepartmentViewset.as_view({"put": "update_department"}),
        name="update-department",
    ),
    path(
        "departments/<str:department_id>/delete/",
        DepartmentViewset.as_view({"delete": "delete_department"}),
        name="update-department",
    ),
    # Employee Status
    path(
        "employee-statuses/",
        EmployeeStatusViewset.as_view({"get": "list_employee_statuses"}),
        name="employee-statuses",
    ),
    path(
        "employee-statuses/add/",
        EmployeeStatusViewset.as_view({"post": "add_employee_status"}),
        name="add-employee-status",
    ),
    path(
        "employee-statuses/<str:employee_status_id>/retrieve/",
        EmployeeStatusViewset.as_view({"get": "retrieve_employee_status"}),
        name="retrieve-employee-status",
    ),
    path(
        "employee-statuses/<str:employee_status_id>/update/",
        EmployeeStatusViewset.as_view({"put": "update_employee_status"}),
        name="update-employee-status",
    ),
    path(
        "employee-statuses/<str:employee_status_id>/delete/",
        EmployeeStatusViewset.as_view({"delete": "delete_employee_status"}),
        name="update-employee-status",
    ),
    # Employees
    path(
        "employees/",
        EmployeeViewset.as_view({"get": "list_employees"}),
        name="employees",
    ),
    path(
        "employees/add/",
        EmployeeViewset.as_view({"post": "add_employee"}),
        name="add-employee",
    ),
    path(
        "employees/<str:employee_id>/retrieve/",
        EmployeeViewset.as_view({"get": "retrieve_employee"}),
        name="retrieve-employee",
    ),
    path(
        "employees/<str:employee_id>/update/",
        EmployeeViewset.as_view({"put": "update_employee"}),
        name="update-employee",
    ),
    path(
        "employees/<str:employee_id>/delete/",
        EmployeeViewset.as_view({"delete": "delete_employee"}),
        name="update-employee",
    ),
    # Equipment Category
    path(
        "equipment-categories/",
        EquipmentCategoryViewset.as_view({"get": "list_equipment_categories"}),
        name="categories",
    ),
    path(
        "equipment-categories/add/",
        EquipmentCategoryViewset.as_view({"post": "add_equipment_category"}),
        name="add-category",
    ),
    path(
        "equipment-categories/<str:category_id>/retrieve/",
        EquipmentCategoryViewset.as_view({"get": "retrieve_equipment_category"}),
        name="retrieve-category",
    ),
    path(
        "equipment-categories/<str:category_id>/update/",
        EquipmentCategoryViewset.as_view({"put": "update_equipment_category"}),
        name="update-category",
    ),
    path(
        "equipment-categories/<str:category_id>/delete/",
        EquipmentCategoryViewset.as_view({"delete": "delete_equipment_category"}),
        name="update-category",
    ),
    # Equipment
    path(
        "equipment/",
        EquipmentViewset.as_view({"get": "list_equipment"}),
        name="equipment",
    ),
    path(
        "equipment/add/",
        EquipmentViewset.as_view({"post": "add_equipment"}),
        name="add-equipment",
    ),
    path(
        "equipment/<str:equipment_id>/retrieve/",
        EquipmentViewset.as_view({"get": "retrieve_equipment"}),
        name="retrieve-equipment",
    ),
    path(
        "equipment/<str:equipment_id>/update/",
        EquipmentViewset.as_view({"put": "update_equipment"}),
        name="update-equipment",
    ),
    path(
        "equipment/<str:equipment_id>/delete/",
        EquipmentViewset.as_view({"delete": "delete_equipment"}),
        name="update-equipment",
    ),
    # Sterlization Method
    path(
        "sterilization-methods/",
        SterilizationMethodViewset.as_view({"get": "list_sterilization_methods"}),
        name="list-sterilization-methods",
    ),
    path(
        "sterilization-methods/add/",
        SterilizationMethodViewset.as_view({"post": "add_sterilization_method"}),
        name="add-sterilization-method",
    ),
    path(
        "sterilization-methods/<str:method_id>/retrieve/",
        SterilizationMethodViewset.as_view({"get": "retrieve_sterilization_method"}),
        name="retrieve-sterilization-method",
    ),
    path(
        "sterilization-methods/<str:method_id>/update/",
        SterilizationMethodViewset.as_view({"put": "update_sterilization_method"}),
        name="update-sterilization-method",
    ),
    path(
        "sterilization-methods/<str:method_id>/delete/",
        SterilizationMethodViewset.as_view({"delete": "delete_sterilization_method"}),
        name="update-sterilization-method",
    ),
    # Batch
    path(
        "batches/",
        BatchViewset.as_view({"get": "list_batches"}),
        name="list-batches",
    ),
    path(
        "batches/add/",
        BatchViewset.as_view({"post": "add_batch"}),
        name="add-batch",
    ),
    path(
        "batches/<str:batch_id>/retrieve/",
        BatchViewset.as_view({"get": "retrieve_batch"}),
        name="retrieve-batch",
    ),
    path(
        "batches/<str:batch_id>/update/",
        BatchViewset.as_view({"put": "update_batch"}),
        name="update-batch",
    ),
    path(
        "batches/<str:batch_id>/delete/",
        BatchViewset.as_view({"delete": "delete_batch"}),
        name="update-batch",
    ),
    # Batch Equipment
    path(
        "batch-equipment/",
        BatchEquipmentViewset.as_view({"get": "list_batch_equipment"}),
        name="list-batch-equipment",
    ),
    path(
        "batch-equipment/add/",
        BatchEquipmentViewset.as_view({"post": "add_batch_equipment"}),
        name="add-batch-equipment",
    ),
    path(
        "batch-equipment/<str:batch_equipment_id>/retrieve/",
        BatchEquipmentViewset.as_view({"get": "retrieve_batch_equipment"}),
        name="retrieve-batch-equipment",
    ),
    path(
        "batch-equipment/<str:batch_equipment_id>/update/",
        BatchEquipmentViewset.as_view({"put": "update_batch_equipment"}),
        name="update-batch-equipment",
    ),
    path(
        "batch-equipment/<str:batch_equipment_id>/delete/",
        BatchEquipmentViewset.as_view({"delete": "delete_batch_equipment"}),
        name="update-batch-equipment",
    ),
    # Stages
    path(
        "stages/",
        StageViewset.as_view({"get": "list_stages"}),
        name="list-stages",
    ),
    path(
        "stages/add/",
        StageViewset.as_view({"post": "add_stage"}),
        name="add-stage",
    ),
    path(
        "stages/<str:stage_id>/retrieve/",
        StageViewset.as_view({"get": "retrieve_stage"}),
        name="retrieve-stage",
    ),
    path(
        "stages/<str:stage_id>/update/",
        StageViewset.as_view({"put": "update_stage"}),
        name="update-stage",
    ),
    path(
        "stages/<str:stage_id>/delete/",
        StageViewset.as_view({"delete": "delete_stage"}),
        name="update-stage",
    ),
    # Operation Logs
    path(
        "operation-logs/",
        OperationLogViewset.as_view({"get": "list_operation_logs"}),
        name="list-operation-log",
    ),
    path(
        "operation-logs/add/",
        OperationLogViewset.as_view({"post": "add_operation_log"}),
        name="add-operation-log",
    ),
    path(
        "operation-logs/<str:log_id>/retrieve/",
        OperationLogViewset.as_view({"get": "retrieve_operation_log"}),
        name="retrieve-operation-log",
    ),
    path(
        "operation-logs/<str:log_id>/update/",
        OperationLogViewset.as_view({"put": "update_operation_log"}),
        name="update-operation-log",
    ),
    path(
        "operation-logs/<str:log_id>/delete/",
        OperationLogViewset.as_view({"delete": "delete_operation_log"}),
        name="update-operation-log",
    ),
    # Packages
    path(
        "packages/",
        PackageViewset.as_view({"get": "list_packages"}),
        name="list-packages",
    ),
    path(
        "packages/add/",
        PackageViewset.as_view({"post": "add_package"}),
        name="add-package",
    ),
    path(
        "packages/<str:package_id>/retrieve/",
        PackageViewset.as_view({"get": "retrieve_package"}),
        name="retrieve-package",
    ),
    path(
        "packages/<str:package_id>/update/",
        PackageViewset.as_view({"put": "update_package"}),
        name="update-package",
    ),
    path(
        "packages/<str:package_id>/delete/",
        PackageViewset.as_view({"delete": "delete_package"}),
        name="update-package",
    ),
    # Package Items
    path(
        "package-items/",
        PackageItemViewset.as_view({"get": "list_package_items"}),
        name="list-package-items",
    ),
    path(
        "package-items/add/",
        PackageItemViewset.as_view({"post": "add_package_item"}),
        name="add-package-item",
    ),
    path(
        "package-items/<str:item_id>/retrieve/",
        PackageItemViewset.as_view({"get": "retrieve_package_item"}),
        name="retrieve-package-item",
    ),
    path(
        "package-items/<str:item_id>/update/",
        PackageItemViewset.as_view({"put": "update_package_item"}),
        name="update-package-item",
    ),
    path(
        "package-items/<str:item_id>/delete/",
        PackageItemViewset.as_view({"delete": "delete_package_item"}),
        name="update-package-item",
    ),
    # Storage Records
    path(
        "storage-records/",
        StorageRecordViewset.as_view({"get": "list_storage_records"}),
        name="list-storage-records",
    ),
    path(
        "storage-records/add/",
        StorageRecordViewset.as_view({"post": "add_storage_record"}),
        name="add-storage-record",
    ),
    path(
        "storage-records/<str:record_id>/retrieve/",
        StorageRecordViewset.as_view({"get": "retrieve_storage_record"}),
        name="retrieve-storage-record",
    ),
    path(
        "storage-records/<str:record_id>/update/",
        StorageRecordViewset.as_view({"put": "update_storage_record"}),
        name="update-storage-record",
    ),
    path(
        "storage-records/<str:record_id>/delete/",
        StorageRecordViewset.as_view({"delete": "delete_storage_record"}),
        name="update-storage-record",
    ),
    # Distribution Record
    path(
        "distribution-records/",
        DistributionRecordViewset.as_view({"get": "list_distribution_records"}),
        name="list-distribution-records",
    ),
    path(
        "distribution-records/add/",
        DistributionRecordViewset.as_view({"post": "add_distribution_record"}),
        name="add-distribution-records",
    ),
    path(
        "distribution-records/<str:record_id>/retrieve/",
        DistributionRecordViewset.as_view({"get": "retrieve_distribution_record"}),
        name="retrieve-distribution-records",
    ),
    path(
        "distribution-records/<str:record_id>/update/",
        DistributionRecordViewset.as_view({"put": "update_distribution_record"}),
        name="update-distribution-records",
    ),
    path(
        "distribution-records/<str:record_id>/delete/",
        DistributionRecordViewset.as_view({"delete": "delete_distribution_record"}),
        name="update-distribution-records",
    ),
    # Login and Code
    path(
        "login/",
        AuthenticationViewset.as_view({"post": "sign_in"}),
        name="login",
    ),
    path(
        "login/get-code/",
        AuthenticationViewset.as_view({"post": "get_code"}),
        name="login-code",
    ),
    path(
        "logout/",
        AuthenticationViewset.as_view({"post": "sign_out"}),
        name="logout",
    ),
]
