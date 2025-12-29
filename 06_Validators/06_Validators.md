# Validation in DRF

In Django, validation refers to the process of checking that the data submitted by a user (e.g. through a form or API) is correct, complete, and in the expected format before it is saved to the database or used in your application.   

DRF Validation ಅಂದರೆ user ಕಳುಹಿಸುವ data ಸರಿಯಾಗಿದೆಯೇ, ತಪ್ಪಿಲ್ಲವೇ ಅಂತ ಪರೀಕ್ಷಿಸಿ, ನಂತರ database ಗೆ save ಮಾಡುವುದು.

Validation ensures data integrity, security, and user-friendly feedback.  

### **Why is Validation Needed**
| English                                  | Kannada                            |
| ---------------------------------------- | ---------------------------------- |
| To avoid invalid data                    | ತಪ್ಪು data database ಗೆ ಹೋಗದಂತೆ     |
| To avoid security issues                 | ಸುರಕ್ಷತೆಗಾಗಿ                       |
| To maintain data quality                 | data ಸರಿ ಮತ್ತು standard ಆಗಿರಲು     |
| To return useful error messages to users | user ಗೆ ಸ್ಪಷ್ಟ error message ಕಾಣಲು |

### **Where Validation Happens in DRF**

Validation happens mainly in Serializers.
```
Client → Serializer (validation) → Database
```

### **Types of validation in Django**
**1. Field-Level Validation**

Validation applied to a single field (one form or model field at a time). In ModelForms or Forms using clean_<fieldname>(). Automatically enforced by field types and attributes (e.g., max_length, blank=False).

You are validating individual values (e.g. age, username format, email validity).

Logic doesn’t depend on other fields.

```
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    age = serializers.IntegerField()

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be 18 or above")
        return value
```

**2. Object-Level (Form or Model-Level) Validation**

Validation that involves multiple fields together or the object as a whole.
- In Forms/ModelForms via clean()
- In Models via clean()

You need to compare or cross check multiple fields (e.g., passwords match, discount < price).

The validation logic depends on more than one field.

```
class BookingSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()

    def validate(self, data):
        if data['end_date'] < data['start_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data
```

**3. Validator Functions and Classes**

Reusable validation logic that can be attached to fields.Directly on model fields using validators=[...]

You want to apply the same validation in multiple places.
The logic is self-contained and doesn’t depend on other fields.
You need parameters (use class-based validators for this).

```
from rest_framework import serializers

def validate_email_domain(value):
    if not value.endswith("@gmail.com"):
        raise serializers.ValidationError("Only Gmail addresses are allowed")
    return value

class ContactSerializer(serializers.Serializer):
    email = serializers.EmailField(validators=[validate_email_domain])
```

**Which One Should Prefer**

| Goal                              | Prefer This Validation Type      |
| --------------------------------- | -------------------------------- |
| Validate one field's format/value | Field-Level (`clean_<field>()`)  |
| Compare two or more fields        | Object-Level (`clean()`)         |
| Reuse logic across models/forms   | Validator Function or Class      |
| Enforce model integrity on save   | Model `clean()` + `full_clean()` |
