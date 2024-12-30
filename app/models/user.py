from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class User(models.Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    hashed_password = fields.CharField(max_length=255)
    is_active = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "users"

    def __str__(self):
        return self.email

# Pydantic models for response/request
User_Pydantic = pydantic_model_creator(User, name="User", exclude=("hashed_password",))
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)