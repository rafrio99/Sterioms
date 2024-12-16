import threading
import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import (
    NotAcceptable,
    NotFound,
    AuthenticationFailed,
    PermissionDenied,
)
from core.services import *
from core.selectors import *
from core.utils import generate_token, send_login_code_brevo


class HealthFacilityViewset(viewsets.ViewSet):
    """API class for managing the implementations of the health facility APIs"""

    def create_facility(self, request):
        login_info = authenticated(request)

        if not login_info.employee.has_role("administrator"):
            context = {
                "detail": "Facility creation denied",
                "status": "failed",
                "errors": {
                    "health_facility": f"You do not have permission to create a health facility"
                },
            }
            raise PermissionDenied(context, status.HTTP_403_FORBIDDEN)

        data = request.data
        facility, err = create_hfacility(data)
        if not facility:
            context = {
                "detail": "Could not add health facility",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Health facility added successfully",
            "status": "success",
            "data": facility_info(get_facility_by_id(facility.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def list_facilities(self, request):
        context = facility_info(get_facilities(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_facility(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Health facility retrieved",
            "status": "success",
            "data": facility_info(facility),
        }
        return Response(context, status=status.HTTP_200_OK)

    def facility_departments(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Health facility departments",
            "status": "success",
            "data": department_info(get_departments_by_facility(facility), many=True),
        }
        return Response(context, status=status.HTTP_200_OK)

    def facility_employees(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Health facility employees",
            "status": "success",
            "data": employee_info(get_employees_by_facility(facility), many=True),
        }
        return Response(context, status=status.HTTP_200_OK)

    def facility_batches(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Health facility batches",
            "status": "success",
            "data": batch_info(get_batches(facility), many=True),
        }
        return Response(context, status=status.HTTP_200_OK)

    def facility_packages(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Health facility packages",
            "status": "success",
            "data": package_info(get_packages(facility), many=True),
        }
        return Response(context, status=status.HTTP_200_OK)

    def facility_storage_records(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Health facility storage records",
            "status": "success",
            "data": storage_record_info(get_storage_records(facility), many=True),
        }
        return Response(context, status=status.HTTP_200_OK)

    def facility_distribution_records(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Health facility distribution records",
            "status": "success",
            "data": distribution_record_info(
                get_distribution_records(facility), many=True
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_facility(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        facility, err = update_hfacility(request.data, facility)
        if not facility:
            context = {
                "detail": "Could not update health facility",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Health facility updated successfully",
            "status": "success",
            "data": facility_info(get_facility_by_id(facility.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_facility(self, request, facility_id):
        facility = get_facility_by_id(facility_id)
        if not facility:
            context = {
                "detail": "Facility not found",
                "status": "failed",
                "errors": {
                    "facility": [f"Invalid facility id '{facility_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        facility.delete()
        context = {
            "detail": "Health facility deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class DepartmentViewset(viewsets.ViewSet):
    """API class for managing the implementations of the health facility APIs"""

    def add_department(self, request):
        data = request.data
        department, err = create_department(data)
        if not department:
            context = {
                "detail": "Could not add department",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Department added successfully",
            "status": "success",
            "data": department_info(get_department_by_id(department.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def list_departments(self, request):
        context = department_info(get_departments(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_department(self, request, department_id):
        department = get_department_by_id(department_id)
        if not department:
            context = {
                "detail": "Department not found",
                "status": "failed",
                "errors": {
                    "department": [
                        f"Invalid department '{department_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "department retrieved",
            "status": "success",
            "data": department_info(department),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_department(self, request, department_id):
        department = get_department_by_id(department_id)
        if not department:
            context = {
                "detail": "department not found",
                "status": "failed",
                "errors": {
                    "department": [
                        f"Invalid department '{department_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        department, err = update_department(request.data, department)
        if not department:
            context = {
                "detail": "Could not update department",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Department updated successfully",
            "status": "success",
            "data": department_info(get_department_by_id(department.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_department(self, request, department_id):
        department = get_department_by_id(department_id)
        if not department:
            context = {
                "detail": "Department not found",
                "status": "failed",
                "errors": {
                    "department": [
                        f"Invalid department '{department_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        department.delete()
        context = {
            "detail": "Department deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class EmployeeStatusViewset(viewsets.ViewSet):
    """API class for managing the implementations of the employee status APIs"""

    def add_employee_status(self, request):
        data = request.data
        emp_status, err = create_employee_status(data)
        if not emp_status:
            context = {
                "detail": "Could not add employee status",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Employee status added successfully",
            "status": "success",
            "data": employee_status_info(
                get_employee_status_by_id(emp_status.get("id"))
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def list_employee_statuses(self, request):
        context = employee_status_info(get_employee_statuses(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_employee_status(self, request, employee_status_id):
        emp_status = get_employee_status_by_id(employee_status_id)
        if not emp_status:
            context = {
                "detail": "Employee status not found",
                "status": "failed",
                "errors": {
                    "employee_status": [
                        f"Invalid employee status '{employee_status_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Employee status retrieved",
            "status": "success",
            "data": employee_status_info(emp_status),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_employee_status(self, request, employee_status_id):
        emp_status = get_employee_status_by_id(employee_status_id)
        if not emp_status:
            context = {
                "detail": "Employee status not found",
                "status": "failed",
                "errors": {
                    "employee_status": [
                        f"Invalid employee status '{employee_status_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        emp_status, err = update_employee_status(request.data, emp_status)
        if not emp_status:
            context = {
                "detail": "Could not update employee status",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Employee status updated successfully",
            "status": "success",
            "data": employee_status_info(
                get_employee_status_by_id(emp_status.get("id"))
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_employee_status(self, request, employee_status_id):
        emp_status = get_employee_status_by_id(employee_status_id)
        if not emp_status:
            context = {
                "detail": "Employee status not found",
                "status": "failed",
                "errors": {
                    "employee_status": [
                        f"Invalid employee status '{employee_status_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        emp_status.delete()
        context = {
            "detail": "Employee status deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class EmployeeViewset(viewsets.ViewSet):
    """API class for managing the implementations of the employees APIs"""

    def add_employee(self, request):
        data = request.data
        employee, err = create_employee(data)
        if not employee:
            context = {
                "detail": "Could not add employee",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Employee added successfully",
            "status": "success",
            "data": employee_info(get_employee_by_id(employee.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def list_employees(self, request):
        context = employee_info(get_employees(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_employee(self, request, employee_id):
        employee = get_employee_by_id(employee_id)
        if not employee:
            context = {
                "detail": "Employee not found",
                "status": "failed",
                "errors": {
                    "employee": [f"Invalid employee '{employee_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Employee retrieved",
            "status": "success",
            "data": employee_info(employee),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_employee(self, request, employee_id):
        employee = get_employee_by_id(employee_id)
        if not employee:
            context = {
                "detail": "Employee not found",
                "status": "failed",
                "errors": {
                    "employee": [f"Invalid employee '{employee_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        employee, err = update_employee(request.data, employee)
        if not employee:
            context = {
                "detail": "Could not update employee",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Employee updated successfully",
            "status": "success",
            "data": employee_info(get_employee_by_id(employee.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_employee(self, request, employee_id):
        employee = get_employee_by_id(employee_id)
        if not employee:
            context = {
                "detail": "Employee not found",
                "status": "failed",
                "errors": {
                    "employee": [f"Invalid employee '{employee_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        employee.delete()
        context = {
            "detail": "Employee deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class EquipmentCategoryViewset(viewsets.ViewSet):
    """API class for managing the implementations of the equipment category APIs"""

    def add_equipment_category(self, request):
        data = request.data
        category, err = create_equipment_category(data)
        if not category:
            context = {
                "detail": "Could not add equipment category",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Equipment category added successfully",
            "status": "success",
            "data": equipment_category_info(
                get_equipment_category_by_id(category.get("id")), request
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def list_equipment_categories(self, request):
        context = equipment_category_info_mul(get_equipment_categories(), request)
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_equipment_category(self, request, category_id):
        category = get_equipment_category_by_id(category_id)
        if not category:
            context = {
                "detail": "Equipment category  not found",
                "status": "failed",
                "errors": {
                    "category": [
                        f"Invalid equipment category  '{category_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Equipment category retrieved",
            "status": "success",
            "data": equipment_category_info(category, request),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_equipment_category(self, request, category_id):
        category = get_equipment_category_by_id(category_id)
        if not category:
            context = {
                "detail": "Equipment category  not found",
                "status": "failed",
                "errors": {
                    "category": [
                        f"Invalid equipment category  '{category_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        category, err = modify_equipment_category(request.data, category)
        if not category:
            context = {
                "detail": "Could not update equipment category ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Equipment category updated successfully",
            "status": "success",
            "data": equipment_category_info(
                get_equipment_category_by_id(category.get("id")), request
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_equipment_category(self, request, category_id):
        category = get_equipment_category_by_id(category_id)
        if not category:
            context = {
                "detail": "Equipment category  not found",
                "status": "failed",
                "errors": {
                    "category": [
                        f"Invalid equipment category  '{category_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        category.delete()
        context = {
            "detail": "Equipment category deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class EquipmentViewset(viewsets.ViewSet):
    """API class for managing the implementations of the equipment APIs"""

    def add_equipment(self, request):
        data = request.data
        equipment, err = create_equipment(data)
        if not equipment:
            context = {
                "detail": "Could not add equipment",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Equipment added successfully",
            "status": "success",
            "data": equipment_info(get_equipment_by_id(equipment.get("id")), request),
        }
        return Response(context, status=status.HTTP_200_OK)

    def list_equipment(self, request):
        context = equipment_info_mul(get_equipments(), request)
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_equipment(self, request, equipment_id):
        equipment = get_equipment_by_id(equipment_id)
        if not equipment:
            context = {
                "detail": "Equipment not found",
                "status": "failed",
                "errors": {
                    "equipment": [f"Invalid equipment  '{equipment_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Equipment retrieved",
            "status": "success",
            "data": equipment_info(equipment, request),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_equipment(self, request, equipment_id):
        equipment = get_equipment_by_id(equipment_id)
        if not equipment:
            context = {
                "detail": "Equipment not found",
                "status": "failed",
                "errors": {
                    "equipment": [f"Invalid equipment  '{equipment_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        equipment, err = modify_equipment(request.data, equipment)
        if not equipment:
            context = {
                "detail": "Could not update equipment ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Equipment updated successfully",
            "status": "success",
            "data": equipment_info(get_equipment_by_id(equipment.get("id")), request),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_equipment(self, request, equipment_id):
        authenticated(request)
        equipment = get_equipment_by_id(equipment_id)
        if not equipment:
            context = {
                "detail": "Equipment not found",
                "status": "failed",
                "errors": {
                    "equipment": [f"Invalid equipment '{equipment_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        equipment.delete()
        context = {
            "detail": "Equipment deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class SterilizationMethodViewset(viewsets.ViewSet):
    """API class for managing the implementations of the sterilization_method APIs"""

    def list_sterilization_methods(self, request):
        context = sterilization_method_info_mul(get_sterilization_methods(), request)
        return Response(context, status=status.HTTP_200_OK)

    def add_sterilization_method(self, request):
        data = request.data
        sterilization_method, err = create_sterilization_method(data)
        if not sterilization_method:
            context = {
                "detail": "Could not add sterilization method",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Sterilization method added successfully",
            "status": "success",
            "data": sterilization_method_info(
                get_sterilization_method_by_id(sterilization_method.get("id")), request
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_sterilization_method(self, request, method_id):
        method = get_sterilization_method_by_id(method_id)
        if not method:
            context = {
                "detail": "Sterilization method not found",
                "status": "failed",
                "errors": {
                    "method": [
                        f"Invalid sterilization method  '{method_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Sterilization method retrieved",
            "status": "success",
            "data": sterilization_method_info(method, request),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_sterilization_method(self, request, method_id):
        method = get_sterilization_method_by_id(method_id)
        if not method:
            context = {
                "detail": "Sterilization method not found",
                "status": "failed",
                "errors": {
                    "method": [
                        f"Invalid sterilization method  '{method_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        method, err = modify_sterilization_method(request.data, method)
        if not method:
            context = {
                "detail": "Could not update sterilization_method ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Sterilization method updated successfully",
            "status": "success",
            "data": sterilization_method_info(
                get_sterilization_method_by_id(method.get("id")), request
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_sterilization_method(self, request, method_id):
        method = get_sterilization_method_by_id(method_id)
        if not method:
            context = {
                "detail": "Sterilization method not found",
                "status": "failed",
                "errors": {
                    "method": [
                        f"Invalid sterilization method '{method_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        method.delete()
        context = {
            "detail": "Sterilization method deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class BatchViewset(viewsets.ViewSet):
    """API class for managing the implementations of the batch APIs"""

    def list_batches(self, request):
        context = batch_info(get_batches(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_batch(self, request):
        authenticated(request)
        data = request.data
        batch_equip = data.get("batch_equipment")
        batch, err = create_batch(data)
        if not batch:
            context = {
                "detail": "Could not add batch",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)

        batch = get_batch_by_id(batch.get("id"))
        errors: list = []
        if batch_equip:
            for equip in batch_equip:
                equip["batch"] = batch.pk
                eq, err = create_batch_equipment(equip)
                if not eq:
                    errors.append({"data": equip, "error": errors})

        # Create the default operation logs
        stages = [get_stage_by_rank(1), get_stage_by_rank(2)]
        for stage in stages:
            op_data = {
                "stage": stage.pk,
                "batch": batch.pk,
                "operator": batch.operator.pk,
            }
            create_operation_log(op_data)

        context = {
            "detail": "Batch added successfully",
            "status": "success",
            "data": batch_info(get_batch_by_id(batch.pk)),
        }
        if errors:
            context.update({"errors": errors})
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_batch(self, request, batch_id):
        batch = get_batch_by_id(batch_id)
        if not batch:
            context = {
                "detail": "Batch not found",
                "status": "failed",
                "errors": {"batch": [f"Invalid batch  '{batch_id}' does not exist"]},
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Batch retrieved",
            "status": "success",
            "data": batch_info(batch),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_batch(self, request, batch_id):
        login_info = authenticated(request)
        batch = get_batch_by_id(batch_id)
        if not batch:
            context = {
                "detail": "Batch not found",
                "status": "failed",
                "errors": {"batch": [f"Invalid batch  '{batch_id}' does not exist"]},
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        if login_info.employee != batch.operator:
            context = {
                "detail": "Batch modification forbidden",
                "status": "failed",
                "errors": {"batch": f"You did not create this batch"},
            }
            raise PermissionDenied(context, status.HTTP_403_FORBIDDEN)

        batch, err = modify_batch(request.data, batch)
        if not batch:
            context = {
                "detail": "Could not update batch ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Batch updated successfully",
            "status": "success",
            "data": batch_info(get_batch_by_id(batch.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_batch(self, request, batch_id):
        login_info = authenticated(request)
        batch = get_batch_by_id(batch_id)
        if not batch:
            context = {
                "detail": "Batch not found",
                "status": "failed",
                "errors": {"batch": [f"Invalid batch '{batch_id}' does not exist"]},
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        if login_info.employee != batch.operator:
            context = {
                "detail": "Batch deletion forbidden",
                "status": "failed",
                "errors": {"batch": f"You did not create this batch"},
            }
            raise PermissionDenied(context, status.HTTP_403_FORBIDDEN)

        batch.delete()
        context = {
            "detail": "Batch deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class BatchEquipmentViewset(viewsets.ViewSet):
    """API class for managing the implementations of the batch equipment APIs"""

    def list_batch_equipment(self, request):
        context = batch_equipment_info(get_batch_equipments(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_batch_equipment(self, request):
        data = request.data
        batch_equipment, err = create_batch_equipment(data)
        if not batch_equipment:
            context = {
                "detail": "Could not add batch_equipment",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Batch equipment added successfully",
            "status": "success",
            "data": batch_equipment_info(
                get_batch_equipment_by_id(batch_equipment.get("id"))
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_batch_equipment(self, request, batch_equipment_id):
        batch_equipment = get_batch_equipment_by_id(batch_equipment_id)
        if not batch_equipment:
            context = {
                "detail": "Batch equipment not found",
                "status": "failed",
                "errors": {
                    "batch_equipment": [
                        f"Invalid batch equipment  '{batch_equipment_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Batch equipment retrieved",
            "status": "success",
            "data": batch_equipment_info(batch_equipment),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_batch_equipment(self, request, batch_equipment_id):
        batch_equipment = get_batch_equipment_by_id(batch_equipment_id)
        if not batch_equipment:
            context = {
                "detail": "Batch equipment not found",
                "status": "failed",
                "errors": {
                    "batch_equipment": [
                        f"Invalid batch equipment  '{batch_equipment_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        batch_equipment, err = modify_batch_equipment(request.data, batch_equipment)
        if not batch_equipment:
            context = {
                "detail": "Could not update batch_equipment ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Batch equipment updated successfully",
            "status": "success",
            "data": batch_equipment_info(
                get_batch_equipment_by_id(batch_equipment.get("id"))
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_batch_equipment(self, request, batch_equipment_id):
        batch_equipment = get_batch_equipment_by_id(batch_equipment_id)
        if not batch_equipment:
            context = {
                "detail": "batch_Equipment not found",
                "status": "failed",
                "errors": {
                    "batch_equipment": [
                        f"Invalid batch equipment '{batch_equipment_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        batch_equipment.delete()
        context = {
            "detail": "batch_Equipment deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class StageViewset(viewsets.ViewSet):
    """API class for managing the implementations of the stage APIs"""

    def list_stages(self, request):
        context = stage_info(get_stages(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_stage(self, request):
        data = request.data
        stage, err = create_stage(data)
        if not stage:
            context = {
                "detail": "Could not add stage",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Stage added successfully",
            "status": "success",
            "data": stage_info(get_stage_by_id(stage.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_stage(self, request, stage_id):
        stage = get_stage_by_id(stage_id)
        if not stage:
            context = {
                "detail": "Stage not found",
                "status": "failed",
                "errors": {"stage": [f"Invalid stage  '{stage_id}' does not exist"]},
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Stage retrieved",
            "status": "success",
            "data": stage_info(stage),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_stage(self, request, stage_id):
        stage = get_stage_by_id(stage_id)
        if not stage:
            context = {
                "detail": "Stage not found",
                "status": "failed",
                "errors": {"stage": [f"Invalid stage  '{stage_id}' does not exist"]},
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        stage, err = modify_stage(request.data, stage)
        if not stage:
            context = {
                "detail": "Could not update stage ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Stage updated successfully",
            "status": "success",
            "data": stage_info(get_stage_by_id(stage.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_stage(self, request, stage_id):
        stage = get_stage_by_id(stage_id)
        if not stage:
            context = {
                "detail": "Stage not found",
                "status": "failed",
                "errors": {"stage": [f"Invalid stage '{stage_id}' does not exist"]},
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        stage.delete()
        context = {
            "detail": "Stage deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class OperationLogViewset(viewsets.ViewSet):
    """API class for managing the implementations of the operation log APIs"""

    def list_operation_logs(self, request):
        context = operation_log_info(get_operation_logs(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_operation_log(self, request):
        data = request.data
        log, err = create_operation_log(data)
        if not log:
            context = {
                "detail": "Could not add operation log",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Operation log added successfully",
            "status": "success",
            "data": operation_log_info(get_operation_log_by_id(log.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_operation_log(self, request, log_id):
        log = get_operation_log_by_id(log_id)
        if not log:
            context = {
                "detail": "Operation log not found",
                "status": "failed",
                "errors": {
                    "log": [f"Invalid operation log  '{log_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Operation log retrieved",
            "status": "success",
            "data": operation_log_info(log),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_operation_log(self, request, log_id):
        log = get_operation_log_by_id(log_id)
        if not log:
            context = {
                "detail": "Operation log not found",
                "status": "failed",
                "errors": {
                    "log": [f"Invalid operation log  '{log_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        log, err = modify_operation_log(request.data, log)
        if not log:
            context = {
                "detail": "Could not update operation log ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Operation log updated successfully",
            "status": "success",
            "data": operation_log_info(get_operation_log_by_id(log.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_operation_log(self, request, log_id):
        log = get_operation_log_by_id(log_id)
        if not log:
            context = {
                "detail": "Operation log not found",
                "status": "failed",
                "errors": {"log": [f"Invalid operation log '{log_id}' does not exist"]},
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        log.delete()
        context = {
            "detail": "Operation log deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class PackageViewset(viewsets.ViewSet):
    """API class for managing the implementations of the package APIs"""

    def list_packages(self, request):
        context = package_info(get_packages(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_package(self, request):
        data = request.data
        package_items = data.get("package_items")
        package, err = create_package(data)
        if not package:
            context = {
                "detail": "Could not add package",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)

        package = get_package_by_id(package.get("id"))

        errors: list = []
        if package_items:
            for item in package_items:
                batch = get_batch_by_id(item.get("batch"))
                if not batch.sterilized:
                    errors.append(
                        {"data": item, "error": ["This batch is not sterilized yet"]}
                    )
                    continue
                if batch.packed:
                    errors.append(
                        {"data": item, "error": ["This batch is already packaged"]}
                    )
                    continue

                item["package"] = package.pk

                eq, err = create_package_item(item)
                if not eq:
                    errors.append({"data": item, "error": errors})

                # Create the operation log for packaging the batches
                stage = get_stage_by_rank(5)
                op_data = {
                    "stage": stage.pk,
                    "batch": item.get("batch"),
                    "operator": package.operator.pk,
                }
                create_operation_log(op_data)

            # Did we get all errors?
            if len(errors) == len(package_items):
                context = {
                    "detail": "Could not create package",
                    "status": "failed",
                    "errors": errors,
                }
                package.delete()
                raise NotAcceptable(context)
        batch.completed = True
        batch.date_completed = datetime.datetime.now()
        batch.save()
        context = {
            "detail": "Package added successfully",
            "status": "success",
            "data": package_info(package),
        }
        if errors:
            context.update({"errors": errors})
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_package(self, request, package_id):
        package = get_package_by_id(package_id)
        if not package:
            context = {
                "detail": "Package not found",
                "status": "failed",
                "errors": {
                    "package": [f"Invalid package  '{package_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Package retrieved",
            "status": "success",
            "data": package_info(package),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_package(self, request, package_id):
        package = get_package_by_id(package_id)
        if not package:
            context = {
                "detail": "Package not found",
                "status": "failed",
                "errors": {
                    "package": [f"Invalid package  '{package_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        package, err = modify_package(request.data, package)
        if not package:
            context = {
                "detail": "Could not update package ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Package updated successfully",
            "status": "success",
            "data": package_info(get_package_by_id(package.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_package(self, request, package_id):
        package = get_package_by_id(package_id)
        if not package:
            context = {
                "detail": "Package not found",
                "status": "failed",
                "errors": {
                    "package": [f"Invalid package '{package_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        # Delete the operation logs
        for batch in package.batches_in_package:
            for log in batch.get_log_geq(stage=5):
                log.delete()

        package.delete()
        context = {
            "detail": "Package deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class PackageItemViewset(viewsets.ViewSet):
    """API class for managing the implementations of the package item APIs"""

    def list_package_items(self, request: HttpRequest):
        context = package_item_info(get_package_items(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_package_item(self, request):
        data = request.data
        item, err = create_package_item(data)
        if not item:
            context = {
                "detail": "Could not add package item",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Package item added successfully",
            "status": "success",
            "data": package_item_info(get_package_item_by_id(item.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_package_item(self, request, item_id):
        item = get_package_item_by_id(item_id)
        if not item:
            context = {
                "detail": "Package item not found",
                "status": "failed",
                "errors": {
                    "item": [f"Invalid package item  '{item_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Package item retrieved",
            "status": "success",
            "data": package_item_info(item),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_package_item(self, request, item_id):
        item = get_package_item_by_id(item_id)
        if not item:
            context = {
                "detail": "Package item not found",
                "status": "failed",
                "errors": {
                    "item": [f"Invalid package item  '{item_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        item, err = modify_package_item(request.data, item)
        if not item:
            context = {
                "detail": "Could not update package item ",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Package item updated successfully",
            "status": "success",
            "data": package_item_info(get_package_item_by_id(item.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_package_item(self, request, item_id):
        item = get_package_item_by_id(item_id)
        if not item:
            context = {
                "detail": "Package item not found",
                "status": "failed",
                "errors": {
                    "item": [f"Invalid package item '{item_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        item.delete()
        context = {
            "detail": "Package item deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class StorageRecordViewset(viewsets.ViewSet):
    """API class for managing the implementations of the storage record APIs"""

    def list_storage_records(self, request):
        context = storage_record_info(get_storage_records(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_storage_record(self, request):
        data = request.data
        if package_in_storage(data.get("package")):
            context = {
                "detail": "Package already in store",
                "status": "failed",
                "errors": {"package": ["Pacakge has been stored already"]},
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)

        record, err = create_storage_record(data)
        if not record:
            context = {
                "detail": "Could not add storage record",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)

        # Create the operation log for storing the batches in a package
        package = get_package_by_id(data.get("package"))
        stage = get_stage_by_rank(6)

        errors: list = []
        for item in package.package_items:
            op_data = {
                "stage": stage.pk,
                "batch": item.batch.pk,
                "operator": package.operator.pk,
            }
            _, err = create_operation_log(op_data)
            if err:
                errors.append({"data": item, "error": err})

        context = {
            "detail": "Storage record added successfully",
            "status": "success",
            "data": storage_record_info(get_storage_record_by_id(record.get("id"))),
        }
        if errors:
            context.update({"errors": errors})
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_storage_record(self, request, record_id):
        record = get_storage_record_by_id(record_id)
        if not record:
            context = {
                "detail": "Storage record not found",
                "status": "failed",
                "errors": {
                    "record": [f"Invalid storage record  '{record_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Storage record retrieved",
            "status": "success",
            "data": storage_record_info(record),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_storage_record(self, request, record_id):
        record = get_storage_record_by_id(record_id)
        if not record:
            context = {
                "detail": "Storage record not found",
                "status": "failed",
                "errors": {
                    "record": [f"Invalid storage record  '{record_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        record, err = modify_storage_record(request.data, record)
        if not record:
            context = {
                "detail": "Could not update storage record",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Storage record updated successfully",
            "status": "success",
            "data": storage_record_info(get_storage_record_by_id(record.get("id"))),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_storage_record(self, request, record_id):
        record = get_storage_record_by_id(record_id)
        if not record:
            context = {
                "detail": "Storage record not found",
                "status": "failed",
                "errors": {
                    "record": [f"Invalid storage record '{record_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        # Delete the logs
        for batch in record.package.batches_in_package:
            for log in batch.get_log_geq(stage=6):
                log.delete()

        record.delete()
        context = {
            "detail": "Storage record deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class DistributionRecordViewset(viewsets.ViewSet):
    """API class for managing the implementations of the distribution record APIs"""

    def list_distribution_records(self, request):
        context = distribution_record_info(get_distribution_records(), many=True)
        return Response(context, status=status.HTTP_200_OK)

    def add_distribution_record(self, request):
        data = request.data
        if package_distributed(data.get("package")):
            context = {
                "detail": "Package already distributed",
                "status": "failed",
                "errors": {"package": ["Pacakge has been distributed already"]},
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)

        record, err = create_distribution_record(data)
        if not record:
            context = {
                "detail": "Could not add distribution record",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)

        # Create the operation log for storing the batches in a package
        package = get_package_by_id(record.get("package"))
        stage = get_stage_by_rank(7)
        for item in package.package_items:
            op_data = {
                "stage": stage.pk,
                "batch": item.batch.pk,
                "operator": record.get("operator"),
            }
            create_operation_log(op_data)

        record = get_distribution_record_by_id(record.get("id"))
        record.sent_status = True
        record.date_sent = datetime.datetime.now()
        record.save()

        context = {
            "detail": "Distribution record added successfully",
            "status": "success",
            "data": distribution_record_info(record),
        }
        return Response(context, status=status.HTTP_200_OK)

    def retrieve_distribution_record(self, request, record_id):
        record = get_distribution_record_by_id(record_id)
        if not record:
            context = {
                "detail": "Distribution record not found",
                "status": "failed",
                "errors": {
                    "record": [
                        f"Invalid distribution record '{record_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        context = {
            "detail": "Distribution record retrieved",
            "status": "success",
            "data": distribution_record_info(record),
        }
        return Response(context, status=status.HTTP_200_OK)

    def update_distribution_record(self, request, record_id):
        record = get_distribution_record_by_id(record_id)
        if not record:
            context = {
                "detail": "Distribution record not found",
                "status": "failed",
                "errors": {
                    "record": [
                        f"Invalid distribution record  '{record_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        record, err = modify_distribution_record(request.data, record)
        if not record:
            context = {
                "detail": "Could not update distribution record",
                "status": "failed",
                "errors": err,
            }
            raise NotAcceptable(context, status.HTTP_406_NOT_ACCEPTABLE)
        context = {
            "detail": "Distribution record updated successfully",
            "status": "success",
            "data": distribution_record_info(
                get_distribution_record_by_id(record.get("id"))
            ),
        }
        return Response(context, status=status.HTTP_200_OK)

    def delete_distribution_record(self, request, record_id):
        record = get_distribution_record_by_id(record_id)
        if not record:
            context = {
                "detail": "Distribution record not found",
                "status": "failed",
                "errors": {
                    "record": [
                        f"Invalid distribution record '{record_id}' does not exist"
                    ]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)

        # Delete the operation logs
        for batch in record.package.batches_in_package:
            for log in batch.get_log_geq(stage=7):
                log.delete()

        record.delete()
        context = {
            "detail": "Distribution record deleted successfully",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)


class AuthenticationViewset(viewsets.ViewSet):
    def sign_in(self, request):
        employee_id = request.data.get("employee_id")
        login_code = request.data.get("login_code")
        employee = get_employee_by_id(employee_id)
        if not employee:
            context = {
                "detail": "Employee not found",
                "status": "failed",
                "errors": {
                    "employee": [f"Invalid employee '{employee_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        code = get_login_code(employee)
        if not code:
            context = {
                "detail": "Authentication failed",
                "status": "failed",
                "errors": {"login_code": [f"Get a new login code"]},
            }
            raise AuthenticationFailed(context, status.HTTP_401_UNAUTHORIZED)
        if code.code.strip() != login_code.strip():
            context = {
                "detail": "Authentication failed",
                "status": "failed",
                "errors": {"login_code": [f"Invalid login code"]},
            }
            raise AuthenticationFailed(context, status.HTTP_401_UNAUTHORIZED)

        login, err = add_login_info(
            {"employee": employee.pk, "token": generate_token()}
        )
        if not login:
            context = {
                "detail": "Authentication failed",
                "status": "failed",
                "errors": err,
            }
            raise AuthenticationFailed(context, status.HTTP_401_UNAUTHORIZED)
        code.delete()
        context = {
            "detail": "Successfully signed in",
            "status": "success",
            "data": employee_info(employee),
            "access_token": f"{login.get('employee')}+{login.get('token')}",
        }
        return Response(context, status=status.HTTP_200_OK)

    def get_code(self, request):
        employee_id = request.data.get("employee_id")
        employee = get_employee_by_id(employee_id)
        if not employee:
            context = {
                "detail": "Employee not found",
                "status": "failed",
                "errors": {
                    "employee": [f"Invalid employee '{employee_id}' does not exist"]
                },
            }
            raise NotFound(context, status.HTTP_404_NOT_FOUND)
        login_code = get_login_code(employee)
        emailer = threading.Thread(
            target=send_login_code_brevo, args=[employee, login_code]
        )
        emailer.start()

        context = {
            "detail": f"Login code sent to {employee.email}",
            "status": "success",
        }
        return Response(context, status=status.HTTP_200_OK)

    def sign_out(self, request: HttpRequest):
        login_info = authenticated(request)
        login_info.delete()
        context = {"detail": "Logged out successfully", "status": "sucess"}
        return Response(context, status.HTTP_200_OK)
