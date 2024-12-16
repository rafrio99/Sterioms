# API DOUMENTATIONS FOR THE STERIOMS PROJECT
This document provides the relevant information to interface with the APIs for Sterioms.

The `BASE URL` will be determined after deploying to a feasible hosting platform.

This means that all the paths you see here must be prefixed with the base url.

```
BASE_URL: https://sterioms.onrender.com
```
## Authentication  API Class
For all endpoints that require authorization/authentication, you must set the `Access-Token` header and give it the value of `access_token`. You get this value whenever you log in.


### Get Login Code
This interface allows to get login code to access their accounts when a valid employee ID is provided.

**Path**
```
/api/login/get-code/
```

**Allowed Methods**
```
POST
```

**Content Type**
```
JSON
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"employee_id": str
}
```

**Response Payload**
```json
{
	"detail": "Login code sent to {email or phone}",
	"status": "success"
}
```

### Log In
Log an employee into the system using this endpoint

**Path**
```
/api/login/
```

**Allowed Methods**
```
POST
```

**Content Type**
```
JSON
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"employee_id": str,
	"login_code": str
}
```

**Response Payload**
```json
{
	"detail": "Successfully signed in",
	"status": "success",
	"data": {
		"id": "241017479669",
		"first_name": "Fred",
		"last_name": "Doe Jr.",
		"email": "gfreddoe@gmail.com",
		"phone": "+8619048090841",
		"barcode": "http://localhost:8000/media/barcodes/employees/241017479669.png",
		"date_added": "2024-10-17T09:09:53.119031Z",
		"department": {
			"id": "HD2410152001",
			"name": "Department of surgery",
			"barcode": null,
			"date_added": "2024-10-14T16:41:20.421683Z",
			"health_facility": {
				"id": "HF2410141001",
				"name": "Fred Doe International Hospital",
				"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
				"phone": "+8619048090841",
				"email": "gfreddoe@gmail.com",
				"barcode": null,
				"date_added": "2024-10-14T13:37:25.242377Z"
			}
		},
		"status": null,
		"roles": []
	},
	"access_token": "241017479669+qcHGBx69LRjCZTlG2ADp4SQ2h"
}
```

### Log Out
Log out an employee from the system using this endpoint. 

You must pass the `access_token` as a value to the header `Access-Token` in your request. For example,

**Request Header**
```
Access-Token: access_token_value
```

**Path**
```
/api/logout/
```

**Allowed Methods**
```
POST
```

**Content Type**
```
JSON
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"employee_id": str,
	"login_code": str
}
```

**Response Payload**
```json
{
	"detail": "Logged out successfully",
	"status": "sucess"
}
```

## Health Facility API Class

### List Health Facilities
This endpooint allows you to view all the available health facilities

**Path**
```
/api/facilities/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"name": str,
		"address": str,
		"phone": str,
		"email": str,
		"date_added": datetime
	}
]
```

**Example Response**
```json
[
	{
		"id": "HF2410141001",
		"name": "Fred Doe International Hospital",
		"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
		"phone": "+8619048090841",
		"email": "gfreddoe@gmail.com",
		"date_added": "2024-10-14T13:37:25.242377Z"
	},
	{
		"id": "HF2410141002",
		"name": "Fred Doe International Hospital 2",
		"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
		"phone": "+8619048090842",
		"email": "gdoe@gmail.com",
		"date_added": "2024-10-14T14:07:51.495824Z"
	}
]
```

### Health Facility Departments
This endpoint allows you to retrieve and view the departments in a health facility

**Path**
```
/api/facilities/{facility_id}/departments/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
facility_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**

**Example Response**
```json
{
	"detail": "Health facility departments",
	"status": "success",
	"data": [
		{
			"id": "HD2410152001",
			"name": "Department of surgery",
			"barcode": null,
			"date_added": "2024-10-14T16:41:20.421683Z",
			"health_facility": {
				"id": "HF2410141001",
				"name": "Fred Doe International Hospital",
				"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
				"phone": "+8619048090841",
				"email": "gfreddoe@gmail.com",
				"barcode": null,
				"date_added": "2024-10-14T13:37:25.242377Z"
			}
		},
		{
			"id": "HD2410152002",
			"name": "Department of neurology",
			"barcode": null,
			"date_added": "2024-10-14T17:06:42.364399Z",
			"health_facility": {
				"id": "HF2410141001",
				"name": "Fred Doe International Hospital",
				"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
				"phone": "+8619048090841",
				"email": "gfreddoe@gmail.com",
				"barcode": null,
				"date_added": "2024-10-14T13:37:25.242377Z"
			}
		},
		{
			"id": "HD2410152004",
			"name": "Department of cardiology",
			"barcode": null,
			"date_added": "2024-10-15T11:35:18.610268Z",
			"health_facility": {
				"id": "HF2410141001",
				"name": "Fred Doe International Hospital",
				"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
				"phone": "+8619048090841",
				"email": "gfreddoe@gmail.com",
				"barcode": null,
				"date_added": "2024-10-14T13:37:25.242377Z"
			}
		},
		{
			"id": "HD2410207538",
			"name": "mobile",
			"barcode": "http://localhost:8000/media/barcodes/department/HD2410207538.png",
			"date_added": "2024-10-20T04:03:34.748646Z",
			"health_facility": {
				"id": "HF2410141001",
				"name": "Fred Doe International Hospital",
				"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
				"phone": "+8619048090841",
				"email": "gfreddoe@gmail.com",
				"barcode": null,
				"date_added": "2024-10-14T13:37:25.242377Z"
			}
		}
	]
}
```

### Health Facility Employees
This endpoint allows you to retrieve and view the employees of a health facility

**Path**
```
/api/facilities/{facility_id}/employees/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
facility_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**

**Example Response**
```json
{
	"detail": "Health facility employees",
	"status": "success",
	"data": [
		{
			"id": "241017479669",
			"first_name": "Godfred",
			"last_name": "Doe",
			"email": "asheer@gmail.com",
			"phone": "+8615062275385",
			"barcode": "http://localhost:8000/media/barcodes/employees/241017479669.png",
			"date_added": "2024-10-17T09:09:53.119031Z",
			"department": {
				"id": "HD2410152001",
				"name": "Department of surgery",
				"barcode": null,
				"date_added": "2024-10-14T16:41:20.421683Z",
				"health_facility": {
					"id": "HF2410141001",
					"name": "Fred Doe International Hospital",
					"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
					"phone": "+8619048090841",
					"email": "gfreddoe@gmail.com",
					"barcode": null,
					"date_added": "2024-10-14T13:37:25.242377Z"
				}
			},
			"status": null,
			"roles": []
		}
	]
}
```

### Retrieve Health Facility
This endpooint allows you toretrieve and view the details of an existing health facility

**Path**
```
/api/facilities/{facility_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
facility_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"address": str,
		"phone": str,
		"email": str,
		"date_added": datetime
	}
}
```

**Example Response**
```json
{
	"detail": "Health facility retrieved",
	"status": "success",
	"data": {
		"id": "HF2410141002",
		"name": "Fred Doe International Hospital 2",
		"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
		"phone": "+8619048090842",
		"email": "gdoe@gmail.com",
		"date_added": "2024-10-14T14:07:51.495824Z"
	}
}
```

### Create Health Facility
This endpooint allows you to add a new health facility

**Path**
```
/api/facilities/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"name": str,
	"address": str,
	"phone": str,
	"email": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"address": str,
		"phone": str,
		"email": str,
		"date_added": datetime
	}
}
```

**Example Response**
```json
{
	"detail": "Health facility added successfully",
	"status": "success",
	"data": {
		"id": "HF2410141002",
		"name": "Fred Doe International Hospital 2",
		"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
		"phone": "+8619048090842",
		"email": "gdoe@gmail.com",
		"date_added": "2024-10-14T14:07:51.495824Z"
	}
}
```

### Update Health Facility
This endpooint allows you to update an existing health facility

**Path**
```
/api/facilities/{facility_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
facility_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"name": str,
	"address": str,
	"phone": str,
	"email": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"address": str,
		"phone": str,
		"email": str,
		"date_added": datetime
	}
}
```

**Example Response**
```json
{
	"detail": "Health facility updated successfully",
	"status": "success",
	"data": {
		"id": "HF2410141002",
		"name": "Soufiane Jdaba International Hospital",
		"address": "Dandelion Street, Pidu, Chengdu, Sichuan, China",
		"phone": "+8619048090101",
		"email": "s.jdaba@gmail.com",
		"date_added": "2024-10-14T14:07:51.495824Z"
	}
}
```

### Delete Health Facility
This endpooint allows you to delete an existing health facility

**Path**
```
/api/facilities/{facility_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
facility_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```
None
```

**Response Payload**
```json
{
	"detail": "Health facility deleted successfully",
	"status": "success"
}
```

## Department API Class

### List Departments
This endpooint allows you to view all the available departments

**Path**
```
/api/departments/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"name": str,
		"date_added": datetime,
		"health_facility": str

	}
]
```

**Example Response**
```json
[
	{
		"id": "HD2410152001",
		"name": "Department of surgery",
		"date_added": "2024-10-14T16:41:20.421683Z",
		"health_facility": "HF2410141001"
	},
	{
		"id": "HD2410152004",
		"name": "Department of cardiology",
		"date_added": "2024-10-15T11:35:18.610268Z",
		"health_facility": "HF2410141001"
	},
	{
		"id": "HD2410152002",
		"name": "Department of neurology",
		"date_added": "2024-10-14T17:06:42.364399Z",
		"health_facility": "HF2410141001"
	}
]
```
### Retrieve Departments
This endpooint allows you toretrieve and view the details of an existing departments

**Path**
```
/api/depatments/{department_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
department_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"date_added": datetime,
		"health_facility": str
	}
}
```

**Example Response**
```json
{
	"detail": "department retrieved",
	"status": "success",
	"data": {
		"id": "HD2410152002",
		"name": "Department of neurology",
		"date_added": "2024-10-14T17:06:42.364399Z",
		"health_facility": "HF2410141001"
	}
}
```
### Create Department
This endpooint allows you to add a new department

**Path**
```
/api/departments/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{

	"name": str,
	"health_facility": str

}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"date_added": datetime,
		"health_facility": str
	}
}
```

**Example Response**
```json
{
	"detail": "Department added successfully",
	"status": "success",
	"data": {
		"id": "HD2410152004",
		"name": "Department of surgery",
		"date_added": "2024-10-15T11:35:18.610268Z",
		"health_facility": "HF2410141001"
	}
}
```
### Update Department
This endpooint allows you to update an existing department

**Path**
```
/api/departments/{departments_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
department_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{

	"name": str,
	"health_facility": str

}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"date_added": datetime,
		"health_facility": str
	}
}
```

**Example Response**
```json
{
	"detail": "Department updated successfully",
	"status": "success",
	"data": {
		"id": "HD2410152002",
		"name": "Department of neurology",
		"date_added": "2024-10-14T17:06:42.364399Z",
		"health_facility": "HF2410141001"
	}
}
```
### Delete Department
This endpooint allows you to delete an existing department

**Path**
```
/api/departments/{department_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
department_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Department deleted successfully",
	"status": "success"
}
```

## Employee Status API Class
### List Employee Statuses
This endpooint allows you to view all the available employee statuses

**Path**
```
/api/employee-statuses/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"name": str,
		"code": str,
		"date_added": datetime

	}
]
```

**Example Response**
```json
[
	{
		"id": "5e2d9832-4d7a-4f01-b792-eabf6fad91f9",
		"name": "Soufiane Jdaba",
		"code": "2001",
		"date_added": "2024-10-15T16:44:18.258771Z"
	},
	{
		"id": "761fcd0f-361e-48b3-a3c0-e552a51bffd1",
		"name": "Godfred Joe",
		"code": "2003",
		"date_added": "2024-10-15T16:48:59.146883Z"
	}
]
```
### Retrieve Employee Statuses
This endpooint allows you toretrieve and view the details of an existing employee status

**Path**
```
/api/demployee-statuses/{employee_status_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
employee_status_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str,
		"date_added": datetime,

	}
}
```

**Example Response**
```json
{
	"detail": "Employee status retrieved",
	"status": "success",
	"data": {
		"id": "761fcd0f-361e-48b3-a3c0-e552a51bffd1",
		"name": "Godfred Joe",
		"code": "2003",
		"date_added": "2024-10-15T16:48:59.146883Z"
	}
}
```
### Create Employee Status
This endpooint allows you to add a new employee status

**Path**
```
/api/employee-statuses/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{

	"name": str,
	"code": str
	
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str,
		"date_added": datetime,

	}
}
```

**Example Response**
```json
{
	"detail": "Employee status added successfully",
	"status": "success",
	"data": {
		"id": "761fcd0f-361e-48b3-a3c0-e552a51bffd1",
		"name": "asheer amar",
		"code": "2002",
		"date_added": "2024-10-15T16:48:59.146883Z"
	}
}
```
### Update Employee Status
This endpooint allows you to update an existing employee status

**Path**
```
/api/employee-statuses/{employee_status_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
employee_status_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{

	"name": str,
	"code": str

}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str,
		"date_added": datetime,
		
	}
}
```

**Example Response**
```json
{
	"detail": "Employee status updated successfully",
	"status": "success",
	"data": {
		"id": "761fcd0f-361e-48b3-a3c0-e552a51bffd1",
		"name": "Godfred Joe",
		"code": "2003",
		"date_added": "2024-10-15T16:48:59.146883Z"
	}
}
```
### Delete Employee Status
This endpooint allows you to delete an existing employee status

**Path**
```
/api/employee-statuses/{employee_status_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
employee_status_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Employee status deleted successfully",
	"status": "success"
}
```

## Employee API Class
### List Employees
This endpooint allows you to view all the available employees

**Path**
```
/api/employees/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"first_name": str,
		"last_name": str,
		"email": str,
		"phone": str,
		"date_added": datetime,
		"department": str,
		"status": str,
		"roles": str
	}
}
```

**Example Response**
```json
[
	{
		"id": "241017764535",
		"first_name": "Fred",
		"last_name": "Doe",
		"email": "ggdoe@gmail.com",
		"phone": "+8619045090842",
		"date_added": "2024-10-16T17:13:45.515101Z",
		"department": null,
		"status": null,
		"roles": []
	},
	{
		"id": "241017649796",
		"first_name": "Godfred",
		"last_name": "Doe",
		"email": null,
		"phone": null,
		"date_added": "2024-10-16T17:24:05.734550Z",
		"department": null,
		"status": null,
		"roles": []
	}
]
```
### Retrieve Employees
This endpooint allows you toretrieve and view the details of an existing employee 

**Path**
```
/api/demployees/{employee_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
employee_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"first_name": str,
		"last_name": str,
		"email": str,
		"phone": str,
		"date_added": datetime,
		"department": str,
		"status": str,
		"roles": str
	}
}
```

**Example Response**
```json
{
	"detail": "Employee retrieved",
	"status": "success",
	"data": {
		"id": "241017649796",
		"first_name": "Soufiane",
		"last_name": "Jdaba",
		"email": "s.jdaba17@gmail.com",
		"phone": null,
		"date_added": "2024-10-16T17:24:05.734550Z",
		"department": null,
		"status": null,
		"roles": []
	}
}
```
### Create Employees
This endpooint allows you to add a new employee 

**Path**
```
/api/employees/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"first_name": str,
	"last_name": str,
	"email": str,
	"phone":str
	"department": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"first_name": str,
		"last_name": str,
		"email": str,
		"phone": str,
		"date_added": datetime,
		"department": str,
		"status": str,
		"roles": str
	}
}
```

**Example Response**
```json
{
	"detail": "Employee added successfully",
	"status": "success",
	"data": {
		"id": "241017479669",
		"first_name": "Godfred",
		"last_name": "Doe",
		"email": "asheer@gmail.com",
		"phone": "+8615062275385",
		"date_added": "2024-10-17T09:09:53.119031Z",
		"department": null,
		"status": null,
		"roles": []
	}
}
```
### Update Employees
This endpooint allows you to update an existing employees

**Path**
```
/api/employees/{employee_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
employee_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"first_name": str,
	"last_name": str,
	"email": str,
	"phone":str
	"department": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"first_name": str,
		"last_name": str,
		"email": str,
		"phone": str,
		"date_added": datetime,
		"department": str,
		"status": str,
		"roles": str
	}
}
```

**Example Response**
```json
{
	"detail": "Employee updated successfully",
	"status": "success",
	"data": {
		"id": "241017649796",
		"first_name": "Soufiane",
		"last_name": "Jdaba",
		"email": "s.jdaba17@gmail.com",
		"phone": null,
		"date_added": "2024-10-16T17:24:05.734550Z",
		"department": null,
		"status": null,
		"roles": []
	}
}
```
### Delete Employee 
This endpooint allows you to delete an existing employee

**Path**
```
/api/employees/{employee_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
employee_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Employee deleted successfully",
	"status": "success"
}
```

## Equipment API Class
### List Equipment
This endpooint allows you to view all the available equipments

**Path**
```
/api/equipment/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"name": str,
		"code": str,
		"category": str
	}
]
```

**Example Response**
```json
[
	{
		"id": "EQP9624101796",
		"name": "Scapel",
		"code": "SCPL",
		"category": null
	},
	{
		"id": "EQP241017965",
		"name": "Razor",
		"code": "151",
		"category": null
	}
]
```
### Retrieve Equipment
This endpooint allows you toretrieve and view the details of an existing equipment

**Path**
```
/api/equipment/{equipment_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
equipment_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str,
		"category": str
	}
}
```

**Example Response**
```json
{
	"detail": "Equipment retrieved",
	"status": "success",
	"data": {
		"id": "EQP241017965",
		"name": "Razor",
		"code": "150",
		"category": null
	}
}
```
### Create Equipment
This endpooint allows you to add a new equipment

**Path**
```
/api/equipment/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"name": str,
	"code": str,
	"category": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str,
		"category": str
	}
}
```

**Example Response**
```json
{
	"detail": "Equipment added successfully",
	"status": "success",
	"data": {
		"id": "EQP241017651",
		"name": "Fork",
		"code": "150",
		"category": null
	}
}
```
### Update Equipment
This endpooint allows you to update an existing equipment

**Path**
```
/api/equipment/{equipment_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
equipment_id: str
```

**Query Parameters**
```
None
```


**Request Payload**
```json
{
	"name": str,
	"code": str,
	"category": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str,
		"category": str
	}
}
```

**Example Response**
```json
{
	"detail": "Equipment updated successfully",
	"status": "success",
	"data": {
		"id": "EQP241017965",
		"name": "Razor",
		"code": "151",
		"category": {
			"id": "EQC241017944",
			"name": "Double edged tools",
			"code": "103"
		}
	}
}
```
### Delete Equipment
This endpooint allows you to delete an existing equipment

**Path**
```
/api/equipment/{equipment_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
equipment_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Equipment deleted successfully",
	"status": "success"
}
```

## Equipment Category API Class
### List Equipment Categories
This endpooint allows you to view all the available equipment categories

**Path**
```
/api/equipment-categories/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"name": str,
		"code": str
	}
]
```

**Example Response**
```json
[
	{
		"id": "EQC241017998",
		"name": "Sharp tools",
		"code": "101"
	},
	{
		"id": "EQC241017944",
		"name": "Double edged tools",
		"code": "103"
	},
	{
		"id": "EQC241017747",
		"name": "Dull tools",
		"code": "102"
	}
]
```
### Retrieve Equipment Category
This endpooint allows you toretrieve and view the details of an existing equipment category

**Path**
```
/api/equipment-categories/{equipment-category_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
equipment-categoriy_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str
	}
}
```

**Example Response**
```json
{
	"detail": "Equipment category retrieved",
	"status": "success",
	"data": {
		"id": "EQC241017998",
		"name": "Sharp tools",
		"code": "101"
	}
}
```
### Create Equipment Category
This endpooint allows you to add a new equipment category

**Path**
```
/api/equipment-categories/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"name": str,
	"code": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str
	}
}
```

**Example Response**
```json
{
	"detail": "Equipment category added successfully",
	"status": "success",
	"data": {
		"id": "EQC241017747",
		"name": "Dull tools",
		"code": "102"
	}
}
```
### Update Equipment Category
This endpooint allows you to update an existing equipment category

**Path**
```
/api/equipment-categories/{equipment-categorY_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
equipment-category_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"name": str,
	"code": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str
	}
}
```

**Example Response**
```json
{
	"detail": "Equipment category updated successfully",
	"status": "success",
	"data": {
		"id": "EQC241017998",
		"name": "Sharp tools",
		"code": "104"
	}
}
```
### Delete Equipment Category
This endpooint allows you to delete an existing equipment category

**Path**
```
/api/equipment-categories/{equipment-category_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
equipment-category_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Equipment category deleted successfully",
	"status": "success"
}
```

## Sterilization Method API Class
### List Sterilization Methods
This endpooint allows you to view all the available sterilization methods

**Path**
```
/api/sterilization-methods/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"name": str,
		"code": str
	}
]
```

**Example Response**
```json
[
	{
		"id": "SM2410172257",
		"name": "Radiation",
		"code": "101"
	},
	{
		"id": "SM2410178860",
		"name": "Dry Heat",
		"code": "102"
	},
	{
		"id": "SM2410171506",
		"name": "Moist Heat",
		"code": "103"
	}
]
```
### Retrieve Sterilization Methods
This endpooint allows you toretrieve and view the details of an existing sterilization method

**Path**
```
/api/sterilization-methods/{sterilization-method_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
sterilization method_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str
	}
}
```

**Example Response**
```json
{
	"detail": "Sterilization method retrieved",
	"status": "success",
	"data": {
		"id": "SM2410171506",
		"name": "Moist Heat",
		"code": "103"
	}
}
```
### Create Sterilization Method
This endpooint allows you to add a new sterilization method

**Path**
```
/api/sterilization-methods/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"name": str,
	"code": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str
	}
}
```

**Example Response**
```json
{
	"detail": "Sterilization method added successfully",
	"status": "success",
	"data": {
		"id": "SM2410171506",
		"name": "Moist Heat",
		"code": "103"
	}
}
```
### Update Sterilization Method
This endpooint allows you to update an existing sterilization method

**Path**
```
/api/sterilization-methods/{sterilization-method_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
sterilization-method_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"name": str,
	"code": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"code": str
	}
}
```

**Example Response**
```json
{
	"detail": "Sterilization method updated successfully",
	"status": "success",
	"data": {
		"id": "SM2410171506",
		"name": "Moist Heat",
		"code": "104"
	}
}
```
### Delete Sterilization Method
This endpooint allows you to delete an existing sterilization method

**Path**
```
/api/sterilization-methods/{sterilization-method_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
sterilization-method_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Sterilization method deleted successfully",
	"status": "success"
}
```

## Sterilization Stages API Class
### List Sterilization Stages
This endpooint allows you to view all the available sterilization stages

**Path**
```
/api/stages/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"name": str,
		"stage_number": int
	}
]
```

**Example Response**
```json
[
	{
		"id": "STG241018401",
		"name": "collection",
		"stage_number": 1
	},
	{
		"id": "STG241018845",
		"name": "washing",
		"stage_number": 3
	}
]
```
### Retrieve Sterilization Stages
This endpooint allows you toretrieve and view the details of an existing sterilization stage

**Path**
```
/api/stages/{stage_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
stage_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"stage_number": int

	}
}
```

**Example Response**
```json
{
	"detail": "Stage retrieved",
	"status": "success",
	"data": {
		"id": "STG241018845",
		"name": "washing",
		"stage_number": 3
	}
}
```
### Create Sterilization Stages
This endpooint allows you to add a new sterilization stage

**Path**
```
/api/stages/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{

	"name": str,
	"stage_number": int
	
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"stage_number": int

	}
}
```

**Example Response**
```json
{
	"detail": "Stage added successfully",
	"status": "success",
	"data": {
		"id": "STG241018307",
		"name": "packaging",
		"stage_number": 4
	}
}
```
### Update Sterilization Stages
This endpooint allows you to update an existing sterilization stage

**Path**
```
/api/stages/{stage_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
stage_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{

	"name": str,
	"satge_number": int

}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"name": str,
		"stage_number": int
		
	}
}
```

**Example Response**
```json
{
	"detail": "Stage updated successfully",
	"status": "success",
	"data": {
		"id": "STG241018845",
		"name": "washing",
		"stage_number": 3
	}
}
```
### Delete Sterilization Stages
This endpooint allows you to delete an existing sterilization stage

**Path**
```
/api/stages/{stage_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
stage_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Stage deleted successfully",
	"status": "success"
}
```

## Batches API Class
### List Batches
This endpooint allows you to view all the available batches

**Path**
```
/api/batches/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
    {
        "id": str,
        "date_created": datetime,
        "completed": bool,
        "date_completed": datetime,
        "sterilization_method": str,
        "operator": str,
        "batch_equipment": [
            {
                "id": str,
                "quantity": number,
                "batch": str,
                "equipment": {
                    "id": str,
                    "name": str,
                    "code": str,
                    "category": {
                        "id": str,
                        "name": str,
                        "code": str
                    }
                }
            }
        ]
    }
]
```

**Example Response**
```json
[
	{
		"id": "BAT241017362",
		"date_created": "2024-10-17T14:41:44.680343Z",
		"completed": false,
		"date_completed": null,
		"sterilization_method": "SM2410172257",
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		},
		"batch_equipment": [
			{
				"id": "BE2410177483",
				"quantity": 12,
				"batch": "BAT241017362",
				"equipment": {
					"id": "EQP9624101796",
					"name": "Scapel",
					"code": "SCPL",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410171824",
				"quantity": 4,
				"batch": "BAT241017362",
				"equipment": {
					"id": "EQP241017965",
					"name": "Razor",
					"code": "151",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410176427",
				"quantity": 6,
				"batch": "BAT241017362",
				"equipment": {
					"id": "EQP241017555",
					"name": "knife",
					"code": "152",
					"category": {
						"id": "EQC241017944",
						"name": "Double edged tools",
						"code": "103"
					}
				}
			}
		]
	},
	{
		"id": "BAT241017170",
		"date_created": "2024-10-17T15:02:24.884866Z",
		"completed": false,
		"date_completed": null,
		"sterilization_method": "SM2410172257",
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		},
		"batch_equipment": [
			{
				"id": "BE2410171728",
				"quantity": 12,
				"batch": "BAT241017170",
				"equipment": {
					"id": "EQP9624101796",
					"name": "Scapel",
					"code": "SCPL",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410171487",
				"quantity": 4,
				"batch": "BAT241017170",
				"equipment": {
					"id": "EQP241017965",
					"name": "Razor",
					"code": "151",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410178473",
				"quantity": 6,
				"batch": "BAT241017170",
				"equipment": {
					"id": "EQP241017555",
					"name": "knife",
					"code": "152",
					"category": {
						"id": "EQC241017944",
						"name": "Double edged tools",
						"code": "103"
					}
				}
			}
		]
	},
	{
		"id": "BAT241017951",
		"date_created": "2024-10-17T15:04:21.933926Z",
		"completed": false,
		"date_completed": null,
		"sterilization_method": "SM2410172257",
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		},
		"batch_equipment": [
			{
				"id": "BE2410176243",
				"quantity": 12,
				"batch": "BAT241017951",
				"equipment": {
					"id": "EQP9624101796",
					"name": "Scapel",
					"code": "SCPL",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410177430",
				"quantity": 4,
				"batch": "BAT241017951",
				"equipment": {
					"id": "EQP241017965",
					"name": "Razor",
					"code": "151",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410177424",
				"quantity": 6,
				"batch": "BAT241017951",
				"equipment": {
					"id": "EQP241017555",
					"name": "knife",
					"code": "152",
					"category": {
						"id": "EQC241017944",
						"name": "Double edged tools",
						"code": "103"
					}
				}
			}
		]
	}
]
```
### Retrieve Batche
This endpooint allows you toretrieve and view the details of an existing batche

**Path**
```
/api/batches/{batche_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
batche_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
        "id": str,
        "date_created": datetime,
        "completed": bool,
        "date_completed": datetime,
        "sterilization_method": str,
        "operator": str,
        "batch_equipment": [
            {
                "id": str,
                "quantity": number,
                "batch": str,
                "equipment": {
                    "id": str,
                    "name": str,
                    "code": str,
                    "category": {
                        "id": str,
                        "name": str,
                        "code": str
                    }
                }
            }
        ]
    }

```

**Example Response**
```json
{
	"detail": "Batch retrieved",
	"status": "success",
	"data": {
		"id": "BAT241018967",
		"date_created": "2024-10-18T13:05:47.400364Z",
		"completed": false,
		"date_completed": null,
		"sterilization_method": "SM2410172257",
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		},
		"batch_equipment": [
			{
				"id": "BE2410185480",
				"quantity": 12,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP9624101796",
					"name": "Scapel",
					"code": "SCPL",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410187263",
				"quantity": 4,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP241017965",
					"name": "Razor",
					"code": "151",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410185217",
				"quantity": 6,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP241017555",
					"name": "knife",
					"code": "152",
					"category": {
						"id": "EQC241017944",
						"name": "Double edged tools",
						"code": "103"
					}
				}
			}
		]
	}
}
```
### Create Batch
This endpooint allows you to add a new batche

**Path**
```
/api/batches/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"sterilization_method": str,
	"operator": str,
	"batch_equipment": [
		{
			"equipment": str,
			"quantity": int
		},
		{
			"equipment": str,
			"quantity": int
		},
		{
			"equipment": str,
			"quantity": int
		}
	]
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
        "id": str,
        "date_created": datetime,
        "completed": bool,
        "date_completed": datetime,
        "sterilization_method": str,
        "operator": str,
        "batch_equipment": [
            {
                "id": str,
                "quantity": number,
                "batch": str,
                "equipment": {
                    "id": str,
                    "name": str,
                    "code": str,
                    "category": {
                        "id": str,
                        "name": str,
                        "code": str
                    }
                }
            }
        ]
    }
```

**Example Response**
```json
{
	"detail": "Batch added successfully",
	"status": "success",
	"data": {
		"id": "BAT241018967",
		"date_created": "2024-10-18T13:05:47.400364Z",
		"completed": false,
		"date_completed": null,
		"sterilization_method": "SM2410172257",
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		},
		"batch_equipment": [
			{
				"id": "BE2410185480",
				"quantity": 12,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP9624101796",
					"name": "Scapel",
					"code": "SCPL",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410187263",
				"quantity": 4,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP241017965",
					"name": "Razor",
					"code": "151",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410185217",
				"quantity": 6,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP241017555",
					"name": "knife",
					"code": "152",
					"category": {
						"id": "EQC241017944",
						"name": "Double edged tools",
						"code": "103"
					}
				}
			}
		]
	}
}
```
### Update Batche
This endpooint allows you to update an existing batch

**Path**
```
/api/batches/{batch_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
batch_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"sterilization_method": str,
	"operator": str,
	"batch_equipment": [
		{
			"equipment": str,
			"quantity": int
		},
		{
			"equipment": str,
			"quantity": int
		},
		{
			"equipment": str,
			"quantity": int
		}
	]
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
        "id": str,
        "date_created": datetime,
        "completed": bool,
        "date_completed": datetime,
        "sterilization_method": str,
        "operator": str,
        "batch_equipment": [
            {
                "id": str,
                "quantity": number,
                "batch": str,
                "equipment": {
                    "id": str,
                    "name": str,
                    "code": str,
                    "category": {
                        "id": str,
                        "name": str,
                        "code": str
                    }
                }
            }
        ]
    }
```

**Example Response**
```json
{
	"detail": "Batch updated successfully",
	"status": "success",
	"data": {
		"id": "BAT241018967",
		"date_created": "2024-10-18T13:05:47.400364Z",
		"completed": false,
		"date_completed": null,
		"sterilization_method": "SM2410172257",
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		},
		"batch_equipment": [
			{
				"id": "BE2410185480",
				"quantity": 12,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP9624101796",
					"name": "Scapel",
					"code": "SCPL",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410187263",
				"quantity": 4,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP241017965",
					"name": "Razor",
					"code": "151",
					"category": {
						"id": "EQC241017998",
						"name": "Sharp tools",
						"code": "104"
					}
				}
			},
			{
				"id": "BE2410185217",
				"quantity": 6,
				"batch": "BAT241018967",
				"equipment": {
					"id": "EQP241017555",
					"name": "knife",
					"code": "152",
					"category": {
						"id": "EQC241017944",
						"name": "Double edged tools",
						"code": "103"
					}
				}
			}
		]
	}
}
```
### Delete Batches
Delete a batch from the batches records.

**Path**
```
/api/batches/{batch_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
batch_id: str
```

**Query Parameters**
```
None
```
**Content Tye**
```json
JSON
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Batch deleted successfully",
	"status": "success"
}
```

## Batch Equipment API Class
### List Batch Equipments
This endpooint allows you to view all the available batch equipments

**Path**
```
/api/batch-equipment/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"quantity": int,
		"batch": str,
		"equipment": {
			"id": int,
			"name": str,
			"code": str,
			"category": {
				"id": str,
				"name": str,
				"code": str
			}
		}
	}
]
```

**Example Response**
```json
[
	{
		"id": "BE2410177483",
		"quantity": 12,
		"batch": "BAT241017362",
		"equipment": {
			"id": "EQP9624101796",
			"name": "Scapel",
			"code": "SCPL",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	},
	{
		"id": "BE2410171824",
		"quantity": 4,
		"batch": "BAT241017362",
		"equipment": {
			"id": "EQP241017965",
			"name": "Razor",
			"code": "151",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	},
	{
		"id": "BE2410176427",
		"quantity": 6,
		"batch": "BAT241017362",
		"equipment": {
			"id": "EQP241017555",
			"name": "knife",
			"code": "152",
			"category": {
				"id": "EQC241017944",
				"name": "Double edged tools",
				"code": "103"
			}
		}
	},
	{
		"id": "BE2410171728",
		"quantity": 12,
		"batch": "BAT241017170",
		"equipment": {
			"id": "EQP9624101796",
			"name": "Scapel",
			"code": "SCPL",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	},
	{
		"id": "BE2410171487",
		"quantity": 4,
		"batch": "BAT241017170",
		"equipment": {
			"id": "EQP241017965",
			"name": "Razor",
			"code": "151",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	},
	{
		"id": "BE2410178473",
		"quantity": 6,
		"batch": "BAT241017170",
		"equipment": {
			"id": "EQP241017555",
			"name": "knife",
			"code": "152",
			"category": {
				"id": "EQC241017944",
				"name": "Double edged tools",
				"code": "103"
			}
		}
	},
	{
		"id": "BE2410176243",
		"quantity": 12,
		"batch": "BAT241017951",
		"equipment": {
			"id": "EQP9624101796",
			"name": "Scapel",
			"code": "SCPL",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	},
	{
		"id": "BE2410177430",
		"quantity": 4,
		"batch": "BAT241017951",
		"equipment": {
			"id": "EQP241017965",
			"name": "Razor",
			"code": "151",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	},
	{
		"id": "BE2410177424",
		"quantity": 6,
		"batch": "BAT241017951",
		"equipment": {
			"id": "EQP241017555",
			"name": "knife",
			"code": "152",
			"category": {
				"id": "EQC241017944",
				"name": "Double edged tools",
				"code": "103"
			}
		}
	}
]
```
### Retrieve Batch Equipment
This endpooint allows you toretrieve and view the details of an existing batch equipment

**Path**
```
/api/batch-equipment/{batch-equipment_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
batch-equipment_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"quantity": int,
		"batch": str,
		"equipment": {
			"id": int,
			"name": str,
			"code": str,
			"category": {
				"id": str,
				"name": str,
				"code": str
			}
		}
	}
}
```

**Example Response**
```json
{
	"detail": "Batch equipment retrieved",
	"status": "success",
	"data": {
		"id": "BE2410177483",
		"quantity": 12,
		"batch": "BAT241017362",
		"equipment": {
			"id": "EQP9624101796",
			"name": "Scapel",
			"code": "SCPL",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	}
}
```
### Create Batch Equipment
This endpooint allows you to add a new batch equipment

**Path**
```
/api/batch-equipment/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"batch": str,
	"equipment": str,
	"quantity": int
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"quantity": int,
		"batch": str,
		"equipment": {
			"id": int,
			"name": str,
			"code": str,
			"category": {
				"id": str,
				"name": str,
				"code": str
			}
		}
	}
}
```

**Example Response**
```json
{
	"detail": "Batch equipment added successfully",
	"status": "success",
	"data": {
		"id": "BE2410181035",
		"quantity": 13,
		"batch": "BAT241017362",
		"equipment": {
			"id": "EQP9624101796",
			"name": "Scapel",
			"code": "SCPL",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	}
}
```
### Update Batch Equipment
This endpooint allows you to update an existing batch equipment

**Path**
```
/api/batch-equipment/{batch-equipment_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
batch-equipment_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"batch": str,
	"equipment": str,
	"quantity": int
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"quantity": int,
		"batch": str,
		"equipment": {
			"id": int,
			"name": str,
			"code": str,
			"category": {
				"id": str,
				"name": str,
				"code": str
			}
		}
	}
}
```

**Example Response**
```json
{
	"detail": "Batch equipment updated successfully",
	"status": "success",
	"data": {
		"id": "BE2410181035",
		"quantity": 14,
		"batch": "BAT241017362",
		"equipment": {
			"id": "EQP9624101796",
			"name": "Scapel",
			"code": "SCPL",
			"category": {
				"id": "EQC241017998",
				"name": "Sharp tools",
				"code": "104"
			}
		}
	}
}
```
### Delete Batch Equipment
This endpooint allows you to delete an existing batch equipment

**Path**
```
/api/batch-equipment/{batch-equipment_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
batch-equipment_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "batch_Equipment deleted successfully",
	"status": "success"
}
```

## Operation Logs API Class
### List Operation Logs
This endpooint allows you to view all the available operation logs

**Path**
```
/api/operation-logs/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"operation_date": datetime,
		"stage": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": int
						}
					}
				}
			]
		},
		"operator": {
			"id": str,
			"first_name": str,
			"last_name": str,
			"email": str,
			"phone": str,
			"date_added": datetime,
			"department": str,
			"status":str,
			"roles": []
		}
	}
]
```

**Example Response**
```json
[
	{
		"id": "241018681916",
		"operation_date": "2024-10-18T13:50:48.072612Z",
		"stage": "STG241018401",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		},
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		}
	},
	{
		"id": "241018206764",
		"operation_date": "2024-10-18T14:06:41.686357Z",
		"stage": "STG241018591",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		},
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		}
	}
]
```
### Retrieve Operation Log
This endpooint allows you toretrieve and view the details of an existing operation log

**Path**
```
/api/operation-logs/{operation-log_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
operation-log_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {

		"id": str,
		"operation_date": datetime,
		"stage": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": int
						}
					}
				}
			]
		},
		"operator": {
			"id": str,
			"first_name": str,
			"last_name": str,
			"email": str,
			"phone": str,
			"date_added": datetime,
			"department": str,
			"status":str,
			"roles": []
		}
	}

```

**Example Response**
```json
{
	"detail": "Operation log retrieved",
	"status": "success",
	"data": {
		"id": "241018108080",
		"operation_date": "2024-10-18T14:11:33.963064Z",
		"stage": "STG241018591",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		},
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		}
	}
}
```
### Create Operation Log
This endpooint allows you to add a new operation log

**Path**
```
/api/operation-logs/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"stage": str,
	"batch": str,
	"operator": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {

		"id": str,
		"operation_date": datetime,
		"stage": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": int
						}
					}
				}
			]
		},
		"operator": {
			"id": str,
			"first_name": str,
			"last_name": str,
			"email": str,
			"phone": str,
			"date_added": datetime,
			"department": str,
			"status":str,
			"roles": []
		}
	}

```

**Example Response**
```json
{
	"detail": "Operation log added successfully",
	"status": "success",
	"data": {
		"id": "241018108080",
		"operation_date": "2024-10-18T14:11:33.963064Z",
		"stage": "STG241018591",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		},
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		}
	}
}
```
### Update Operation Log
This endpooint allows you to update an existing Operation Log

**Path**
```
/api/operation-logs/{operation-log_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
operation-log_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"stage": str,
	"batch": str,
	"operator": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {

		"id": str,
		"operation_date": datetime,
		"stage": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": int
						}
					}
				}
			]
		},
		"operator": {
			"id": str,
			"first_name": str,
			"last_name": str,
			"email": str,
			"phone": str,
			"date_added": datetime,
			"department": str,
			"status":str,
			"roles": []
		}
	}
```

**Example Response**
```json
{
	"detail": "Operation log updated successfully",
	"status": "success",
	"data": {
		"id": "241018108080",
		"operation_date": "2024-10-18T14:11:33.963064Z",
		"stage": "STG241018748",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		},
		"operator": {
			"id": "241017764535",
			"first_name": "Fred",
			"last_name": "Doe",
			"email": "ggdoe@gmail.com",
			"phone": "+8619045090842",
			"date_added": "2024-10-16T17:13:45.515101Z",
			"department": null,
			"status": null,
			"roles": []
		}
	}
}
```
### Delete Operation Log
This endpooint allows you to delete an existing Operation Log

**Path**
```
/api/operation-logs/{operation-log_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
operation-log_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Operation log deleted successfully",
	"status": "success"
}
```

## Packages API Class
### List Packages
This endpooint allows you to view all the available packages

**Path**
```
/api/packages/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"date_packed": datetime,
		"operator": str,
		"receiver": str,
		"package_items": [
			{
				"id": str,
				"package": str,
				"batch": {
					"id": str,
					"date_created": datetime,
					"completed": boolean,
					"date_completed": datetime,
					"sterilization_method": str,
					"operator": {
						"id": str,
						"first_name": str,
						"last_name": str,
						"email": str,
						"phone": str,
						"date_added": datetime,
						"department": str,
						"status": str,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": str,
							"quantity": int,
							"batch": str,
							"equipment": {
								"id": str,
								"name": str,
								"code": str,
								"category": {
									"id": str,
									"name": str,
									"code": str
								}
							}
						}
					]
				}
			}
]
```

**Example Response**
```json
[
	{
		"id": "PKG241018149",
		"date_packed": "2024-10-18T13:05:57.933302Z",
		"operator": "241017764535",
		"receiver": "HD2410152004",
		"package_items": [
			{
				"id": "PKI241018215",
				"package": "PKG241018149",
				"batch": {
					"id": "BAT241017362",
					"date_created": "2024-10-17T14:41:44.680343Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410177483",
							"quantity": 12,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171824",
							"quantity": 4,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410176427",
							"quantity": 6,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018704",
				"package": "PKG241018149",
				"batch": {
					"id": "BAT241017170",
					"date_created": "2024-10-17T15:02:24.884866Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410171728",
							"quantity": 12,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171487",
							"quantity": 4,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410178473",
							"quantity": 6,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018281",
				"package": "PKG241018149",
				"batch": {
					"id": "BAT241017951",
					"date_created": "2024-10-17T15:04:21.933926Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410176243",
							"quantity": 12,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177430",
							"quantity": 4,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177424",
							"quantity": 6,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			}
		]
	}
]
```
### Retrieve Package
This endpooint allows you toretrieve and view the details of an existing package

**Path**
```
/api/packages/{package_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
package_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"date_packed": datetime,
		"operator": str,
		"receiver": str,
		"package_items": [
			{
				"id": str,
				"package": str,
				"batch": {
					"id": str,
					"date_created": datetime,
					"completed": boolean,
					"date_completed": datetime,
					"sterilization_method": str,
					"operator": {
						"id": str,
						"first_name": str,
						"last_name": str,
						"email": str,
						"phone": str,
						"date_added": datetime,
						"department": str,
						"status": str,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": str,
							"quantity": int,
							"batch": str,
							"equipment": {
								"id": str,
								"name": str,
								"code": str,
								"category": {
									"id": str,
									"name": str,
									"code": str
								}
							}
						}
					]
				}
			}
}
```

**Example Response**
```json
{
	"detail": "Package retrieved",
	"status": "success",
	"data": {
		"id": "PKG241018778",
		"date_packed": "2024-10-18T15:15:41.380625Z",
		"operator": "241017764535",
		"receiver": "HD2410152004",
		"package_items": [
			{
				"id": "PKI241018878",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017362",
					"date_created": "2024-10-17T14:41:44.680343Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410177483",
							"quantity": 12,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171824",
							"quantity": 4,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410176427",
							"quantity": 6,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018856",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017170",
					"date_created": "2024-10-17T15:02:24.884866Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410171728",
							"quantity": 12,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171487",
							"quantity": 4,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410178473",
							"quantity": 6,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018151",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017951",
					"date_created": "2024-10-17T15:04:21.933926Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410176243",
							"quantity": 12,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177430",
							"quantity": 4,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177424",
							"quantity": 6,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			}
		]
	}
}
```
### Create Package
This endpooint allows you to add a new package

**Path**
```
/api/packages/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"operator": str,
	"receiver": str,
	"package_items": [
		{
			"batch": str
		},
		{
			"batch": str
		},
		{
			"batch": str
		}
	]
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
				"id": str,
				"package": str,
				"batch": {
					"id": str,
					"date_created": datetime,
					"completed": boolean,
					"date_completed": datetime,
					"sterilization_method": str,
					"operator": {
						"id": str,
						"first_name": str,
						"last_name": str,
						"email": str,
						"phone": str,
						"date_added": datetime,
						"department": str,
						"status": str,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": str,
							"quantity": int,
							"batch": str,
							"equipment": {
								"id": str,
								"name": str,
								"code": str,
								"category": {
									"id": str,
									"name": str,
									"code": str
								}
							}
						}
					]
				}
			}
}
```

**Example Response**
```json
{
	"detail": "Package added successfully",
	"status": "success",
	"data": {
		"id": "PKG241018778",
		"date_packed": "2024-10-18T15:15:41.380625Z",
		"operator": "241017764535",
		"receiver": "HD2410152004",
		"package_items": [
			{
				"id": "PKI241018878",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017362",
					"date_created": "2024-10-17T14:41:44.680343Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410177483",
							"quantity": 12,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171824",
							"quantity": 4,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410176427",
							"quantity": 6,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018856",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017170",
					"date_created": "2024-10-17T15:02:24.884866Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410171728",
							"quantity": 12,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171487",
							"quantity": 4,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410178473",
							"quantity": 6,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018151",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017951",
					"date_created": "2024-10-17T15:04:21.933926Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410176243",
							"quantity": 12,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177430",
							"quantity": 4,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177424",
							"quantity": 6,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			}
		]
	}
}
```
### Update Package
This endpooint allows you to update an existing package

**Path**
```
/api/packages/{package_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
package_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"operator": str,
	"receiver": str,
	"package_items": [
		{
			"batch": str
		},
		{
			"batch": str
		},
		{
			"batch": str
		}
	]
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
				"id": str,
				"package": str,
				"batch": {
					"id": str,
					"date_created": datetime,
					"completed": boolean,
					"date_completed": datetime,
					"sterilization_method": str,
					"operator": {
						"id": str,
						"first_name": str,
						"last_name": str,
						"email": str,
						"phone": str,
						"date_added": datetime,
						"department": str,
						"status": str,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": str,
							"quantity": int,
							"batch": str,
							"equipment": {
								"id": str,
								"name": str,
								"code": str,
								"category": {
									"id": str,
									"name": str,
									"code": str
								}
							}
						}
					]
				}
			}
}
```

**Example Response**
```json
{
	"detail": "Package updated successfully",
	"status": "success",
	"data": {
		"id": "PKG241018778",
		"date_packed": "2024-10-18T15:15:41.380625Z",
		"operator": "241017307672",
		"receiver": "HD2410152004",
		"package_items": [
			{
				"id": "PKI241018878",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017362",
					"date_created": "2024-10-17T14:41:44.680343Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410177483",
							"quantity": 12,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171824",
							"quantity": 4,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410176427",
							"quantity": 6,
							"batch": "BAT241017362",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018856",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017170",
					"date_created": "2024-10-17T15:02:24.884866Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410171728",
							"quantity": 12,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410171487",
							"quantity": 4,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410178473",
							"quantity": 6,
							"batch": "BAT241017170",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			},
			{
				"id": "PKI241018151",
				"package": "PKG241018778",
				"batch": {
					"id": "BAT241017951",
					"date_created": "2024-10-17T15:04:21.933926Z",
					"completed": false,
					"date_completed": null,
					"sterilization_method": "SM2410172257",
					"operator": {
						"id": "241017764535",
						"first_name": "Fred",
						"last_name": "Doe",
						"email": "ggdoe@gmail.com",
						"phone": "+8619045090842",
						"date_added": "2024-10-16T17:13:45.515101Z",
						"department": null,
						"status": null,
						"roles": []
					},
					"batch_equipment": [
						{
							"id": "BE2410176243",
							"quantity": 12,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP9624101796",
								"name": "Scapel",
								"code": "SCPL",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177430",
							"quantity": 4,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017965",
								"name": "Razor",
								"code": "151",
								"category": {
									"id": "EQC241017998",
									"name": "Sharp tools",
									"code": "104"
								}
							}
						},
						{
							"id": "BE2410177424",
							"quantity": 6,
							"batch": "BAT241017951",
							"equipment": {
								"id": "EQP241017555",
								"name": "knife",
								"code": "152",
								"category": {
									"id": "EQC241017944",
									"name": "Double edged tools",
									"code": "103"
								}
							}
						}
					]
				}
			}
		]
	}
}
```
### Delete Packages
This endpooint allows you to delete an existing package

**Path**
```
/api/packages/{package_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
package_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Package deleted successfully",
	"status": "success"
}
```

## Package Items API Class
### List Package Items
This endpooint allows you to view all the available package items

**Path**
```
/api/package-items/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"package": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": str
						}
					}
				}
]
```

**Example Response**
```json
[
	{
		"id": "PKI241018215",
		"package": "PKG241018149",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		}
	},
	{
		"id": "PKI241018704",
		"package": "PKG241018149",
		"batch": {
			"id": "BAT241017170",
			"date_created": "2024-10-17T15:02:24.884866Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410171728",
					"quantity": 12,
					"batch": "BAT241017170",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171487",
					"quantity": 4,
					"batch": "BAT241017170",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410178473",
					"quantity": 6,
					"batch": "BAT241017170",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		}
	},
	{
		"id": "PKI241018281",
		"package": "PKG241018149",
		"batch": {
			"id": "BAT241017951",
			"date_created": "2024-10-17T15:04:21.933926Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410176243",
					"quantity": 12,
					"batch": "BAT241017951",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410177430",
					"quantity": 4,
					"batch": "BAT241017951",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410177424",
					"quantity": 6,
					"batch": "BAT241017951",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		}
	}
]
```
### Retrieve Package Items
This endpooint allows you toretrieve and view the details of an existing package item

**Path**
```
/api/package-items/{package-item_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
package-item_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"package": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": str
						}
					}
				}
]
```

**Example Response**
```json
{
	"detail": "Package item retrieved",
	"status": "success",
	"data": {
		"id": "PKI241018446",
		"package": "PKG241018149",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		}
	}
}
```
### Create Package Items
This endpooint allows you to add a new package item

**Path**
```
/api/package-items/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"package": str,
	"batch": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"package": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": str
						}
					}
				}
]
```

**Example Response**
```json
{
	"detail": "Package item added successfully",
	"status": "success",
	"data": {
		"id": "PKI241018446",
		"package": "PKG241018149",
		"batch": {
			"id": "BAT241017362",
			"date_created": "2024-10-17T14:41:44.680343Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410177483",
					"quantity": 12,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171824",
					"quantity": 4,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410176427",
					"quantity": 6,
					"batch": "BAT241017362",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		}
	}
}
```
### Update Package Items
This endpooint allows you to update an existing package item

**Path**
```
/api/package-items/{package-item_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
package-item_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"package": str,
	"batch": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"package": str,
		"batch": {
			"id": str,
			"date_created": datetime,
			"completed": boolean,
			"date_completed": datetime,
			"sterilization_method": str,
			"operator": {
				"id": str,
				"first_name": str,
				"last_name": str,
				"email": str,
				"phone": str,
				"date_added": datetime,
				"department": str,
				"status": str,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": str,
					"quantity": int,
					"batch": str,
					"equipment": {
						"id": str,
						"name": str,
						"code": str,
						"category": {
							"id": str,
							"name": str,
							"code": str
						}
					}
				}
]
```

**Example Response**
```json
{
	"detail": "Package item updated successfully",
	"status": "success",
	"data": {
		"id": "PKI241018446",
		"package": "PKG241018149",
		"batch": {
			"id": "BAT241017170",
			"date_created": "2024-10-17T15:02:24.884866Z",
			"completed": false,
			"date_completed": null,
			"sterilization_method": "SM2410172257",
			"operator": {
				"id": "241017764535",
				"first_name": "Fred",
				"last_name": "Doe",
				"email": "ggdoe@gmail.com",
				"phone": "+8619045090842",
				"date_added": "2024-10-16T17:13:45.515101Z",
				"department": null,
				"status": null,
				"roles": []
			},
			"batch_equipment": [
				{
					"id": "BE2410171728",
					"quantity": 12,
					"batch": "BAT241017170",
					"equipment": {
						"id": "EQP9624101796",
						"name": "Scapel",
						"code": "SCPL",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410171487",
					"quantity": 4,
					"batch": "BAT241017170",
					"equipment": {
						"id": "EQP241017965",
						"name": "Razor",
						"code": "151",
						"category": {
							"id": "EQC241017998",
							"name": "Sharp tools",
							"code": "104"
						}
					}
				},
				{
					"id": "BE2410178473",
					"quantity": 6,
					"batch": "BAT241017170",
					"equipment": {
						"id": "EQP241017555",
						"name": "knife",
						"code": "152",
						"category": {
							"id": "EQC241017944",
							"name": "Double edged tools",
							"code": "103"
						}
					}
				}
			]
		}
	}
}
```
### Delete Package Items
This endpooint allows you to delete an existing package item

**Path**
```
/api/package-items/{package-item_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
package-item_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Package item deleted successfully",
	"status": "success"
}
```

## Storage records API Class
### List Storage Records
This endpooint allows you to view all the available storage records

**Path**
```
/api/storage-records/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"location": str,
		"storage_number": str,
		"package": str
	}
]
```

**Example Response**
```json
[
	{
		"id": "ST2410191322",
		"location": "Room 1",
		"storage_number": "100",
		"package": "PKG241018149"
	}
]
```
### Retrieve Storage Record
This endpooint allows you toretrieve and view the details of an existing storage record

**Path**
```
/api/storage-records/{storage-record_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
storage-record_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": 	{
		"id": str,
		"location": str,
		"storage_number": str,
		"package": str
	}
}
```

**Example Response**
```json
{
	"detail": "Storage record retrieved",
	"status": "success",
	"data": {
		"id": "ST2410191322",
		"location": "Room 1",
		"storage_number": "100",
		"package": "PKG241018149"
	}
}
```
### Create Storage Record
This endpooint allows you to add a new storage record

**Path**
```
/api/storage-records/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"location": str,
	"storage_number": str,
	"package": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": 	{
		"id": str,
		"location": str,
		"storage_number": str,
		"package": str
	}
}
```

**Example Response**
```json
{
	"detail": "Storage record added successfully",
	"status": "success",
	"data": {
		"id": "ST2410190041",
		"location": "Room 1",
		"storage_number": "100",
		"package": "PKG241018149"
	}
}
```
### Update Storage Record
This endpooint allows you to update an existing storage record

**Path**
```
/api/storage-records/{storage-record_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
storage-record_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"location": str,
	"storage_number": str,
	"package": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": 	{
		"id": str,
		"location": str,
		"storage_number": str,
		"package": str
	}
}
```

**Example Response**
```json
{
	"detail": "Storage record updated successfully",
	"status": "success",
	"data": {
		"id": "ST2410191322",
		"location": "Room 2",
		"storage_number": "101",
		"package": "PKG241018149"
	}
}
```
### Delete Storage Record
This endpooint allows you to delete an existing  storage record

**Path**
```
/api/storage-records/{storage-record_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
storage-record_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Storage record deleted successfully",
	"status": "success"
}
```

## Distribution records API Class
### List Distribution Records
This endpooint allows you to view all the available distribution records

**Path**
```
/api/distribution-records/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
[
	{
		"id": str,
		"sent_status": boolean,
		"date_sent": datetime,
		"receive_status": boolean,
		"date_received": datetime,
		"package": str,
		"operator": str
	}
]
```

**Example Response**
```json
[
	{
		"id": "241019900178",
		"sent_status": false,
		"date_sent": null,
		"receive_status": false,
		"date_received": null,
		"package": "PKG241018149",
		"operator": "241017764535"
	}
]
```
### Retrieve Distribution Record
This endpooint allows you toretrieve and view the details of an existing Distribution Record

**Path**
```
/api/distribution-records/{distribution-record_id}/retrieve/
```

**Allowed Methods**
```
GET
```

**Path Parameters**
```
distribution-record_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"sent_status": boolean,
		"date_sent": datetime,
		"receive_status": boolean,
		"date_received": datetime,
		"package": str,
		"operator": str
	}
}
```

**Example Response**
```json
{
	"detail": "Distribution record retrieved",
	"status": "success",
	"data": {
		"id": "241019900178",
		"sent_status": false,
		"date_sent": null,
		"receive_status": false,
		"date_received": null,
		"package": "PKG241018149",
		"operator": "241017764535"
	}
}
```
### Create Distribution Record
This endpooint allows you to add a new distribution record

**Path**
```
/api/distribution-records/add/
```

**Allowed Methods**
```
POST
```

**Path Parameters**
```
None
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"package": str,
	"operator": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"sent_status": boolean,
		"date_sent": datetime,
		"receive_status": boolean,
		"date_received": datetime,
		"package": str,
		"operator": str
	}
}
```

**Example Response**
```json
{
	"detail": "Distribution record added successfully",
	"status": "success",
	"data": {
		"id": "241019900178",
		"sent_status": false,
		"date_sent": null,
		"receive_status": false,
		"date_received": null,
		"package": "PKG241018149",
		"operator": "241017764535"
	}
}
```
### Update Distribution Record
This endpooint allows you to update an existing distribution record

**Path**
```
/api/distribution-records/{distribution-record_id}/update/
```

**Allowed Methods**
```
PUT
```

**Path Parameters**
```
distribution-record_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
{
	"package": str,
	"operator": str
}
```

**Response Payload**
```json
{
	"detail": str,
	"status": str,
	"data": {
		"id": str,
		"sent_status": boolean,
		"date_sent": datetime,
		"receive_status": boolean,
		"date_received": datetime,
		"package": str,
		"operator": str
	}
}
```

**Example Response**
```json
{
	"detail": "Distribution record updated successfully",
	"status": "success",
	"data": {
		"id": "241019900178",
		"sent_status": false,
		"date_sent": null,
		"receive_status": false,
		"date_received": null,
		"package": "PKG241018149",
		"operator": "241017307672"
	}
}
```
### Delete Distribution Record
This endpooint allows you to delete an existing Distribution Record

**Path**
```
/api/distribution-records/{distribution-record_id}/delete/
```

**Allowed Methods**
```
DELETE
```

**Path Parameters**
```
distribution-record_id: str
```

**Query Parameters**
```
None
```

**Request Payload**
```json
None
```

**Response Payload**
```json
{
	"detail": "Distribution record deleted successfully",
	"status": "success"
}
```
