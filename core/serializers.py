from rest_framework import serializers
from core.models import (
    HealthFacility,
    Department,
    EmployeeStatus,
    Employee,
    Equipment,
    EquipmentCategory,
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
    Role,
)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

    def validate(self, data):
        return data


class HealthFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFacility
        fields = "__all__"

    def validate(self, data):
        return data


class DepartmentSerializer(serializers.ModelSerializer):
    health_facility = serializers.PrimaryKeyRelatedField(
        queryset=HealthFacility.objects.all(), write_only=True
    )
    health_facility_data = HealthFacilitySerializer(
        source="health_facility", read_only=True
    )

    class Meta:
        model = Department
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["health_facility"] = data.pop("health_facility_data")
        return data


class EmployeeStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeStatus
        fields = "__all__"

    def validate(self, data):
        return data


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), write_only=True
    )
    department_data = DepartmentSerializer(source="department", read_only=True)

    status = serializers.PrimaryKeyRelatedField(
        queryset=EmployeeStatus.objects.all(), write_only=True
    )
    status_data = EmployeeStatusSerializer(source="status", read_only=True)

    roles = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), write_only=True, many=True
    )
    roles_data = RoleSerializer(source="roles", read_only=True, many=True)

    class Meta:
        model = Employee
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["department"] = data.pop("department_data")
        data["status"] = data.pop("status_data")
        data["roles"] = data.pop("roles_data")
        return data


class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class SterilizationMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = SterilizationMethod
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class BatchSerializer(serializers.ModelSerializer):
    operator = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), write_only=True
    )
    op_data = EmployeeSerializer(source="operator", read_only=True)

    sterilization_method = serializers.PrimaryKeyRelatedField(
        queryset=SterilizationMethod.objects.all(), write_only=True
    )
    sm_data = SterilizationMethodSerializer(
        source="sterilization_method", read_only=True
    )

    class Meta:
        model = Batch
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["operator"] = data.pop("op_data")
        data["sterilization_method"] = data.pop("sm_data")
        data["batch_equipment"] = BatchEquipmentSerializer(
            instance.batch_equipment, many=True
        ).data
        data["stages"] = StageSerializer(instance.stages, many=True).data
        data["current_stage"] = StageSerializer(instance.current_stage).data
        return data


class BatchEquipmentSerializer(serializers.ModelSerializer):
    equipment = serializers.PrimaryKeyRelatedField(
        queryset=Equipment.objects.all(), write_only=True
    )
    equipment_data = EquipmentSerializer(source="equipment", read_only=True)

    class Meta:
        model = BatchEquipment
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class OperationLogSerializer(serializers.ModelSerializer):
    operator = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), write_only=True
    )
    op_data = EmployeeSerializer(source="operator", read_only=True)

    stage = serializers.PrimaryKeyRelatedField(
        queryset=Stage.objects.all(), write_only=True
    )
    stage_data = StageSerializer(source="stage", read_only=True)

    class Meta:
        model = OperationLog
        fields = "__all__"

    def validate(self, data):
        batch = data.get("batch")
        stage = data.get("stage")
        if batch.current_stage:
            if batch.current_stage.stage_number > stage.stage_number:
                raise serializers.ValidationError(
                    {
                        "stage": f"Batch cannot move to previous stage. This batch already passed '{stage.name}' stage"
                    }
                )
            if batch.current_stage.stage_number == stage.stage_number:
                raise serializers.ValidationError(
                    {"stage": f"Batch is already in the '{stage.name}' stage"}
                )
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["stage"] = data.pop("stage_data")
        data["operator"] = data.pop("op_data")
        return data


class PackageSerializer(serializers.ModelSerializer):
    operator = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(), write_only=True
    )
    op_data = EmployeeSerializer(source="operator", read_only=True)
    receiver = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), write_only=True
    )
    receiver_data = DepartmentSerializer(source="receiver", read_only=True)

    class Meta:
        model = Package
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["operator"] = data.pop("op_data")
        data["receiver"] = data.pop("receiver_data")
        data["stored"] = instance.stored
        data["distributed"] = instance.distributed
        # print(instance.package_items)
        data["package_items"] = PackageItemSerializer(
            instance.package_items, many=True
        ).data
        return data


class PackageItemSerializer(serializers.ModelSerializer):
    # batch = serializers.PrimaryKeyRelatedField(
    #     queryset=Batch.objects.all(), write_only=True
    # )
    # batch_data = BatchSerializer(source="batch", read_only=True)

    class Meta:
        model = PackageItem
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data["batch"] = data.pop("batch_data")
        return data


class StorageRecordSerializer(serializers.ModelSerializer):
    package = serializers.PrimaryKeyRelatedField(
        queryset=Package.objects.all(), write_only=True
    )
    package_data = PackageSerializer(source="package", read_only=True)

    class Meta:
        model = StorageRecord
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["package"] = data.pop("package_data")
        data["distributed"] = instance.distributed
        return data


class DistributionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionRecord
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class DistributionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionRecord
        fields = "__all__"

    def validate(self, data):
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class LoginCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginCode
        fields = "__all__"

    def validate(self, data):
        return data


class LoginTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginTable
        fields = "__all__"

    def validate(self, data):
        return data
