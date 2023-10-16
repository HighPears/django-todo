from django import forms
from .models import Todo


class AddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            "todo_title",
            "todo_memo",
        ]
        widgets = {
            "todo_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Title",
                    "size": "60",
                }
            ),
            "todo_memo": forms.Textarea(),
        }
        labels = {"todo_title": "件名", "todo_memo": "メモ"}
        help_texts = {
            "todo_title": "作成するTodoのタイトルを入力",
            "todo_memo": "Todoのメモを入力",
        }
        error_messages = {
            "todo_title": {
                "required": "件名は必須です",
                "max_length": "件名は256文字まで入力できます",
            }
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["todo_title", "todo_memo", "todo_visible"]
        widgets = {
            "todo_title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Title",
                    "size": "100",
                }
            ),
            "todo_memo": forms.Textarea(attrs={"class": "form-control"}),
            "todo_visible": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }
        labels = {
            "todo_title": "件名",
            "todo_memo": "メモ",
            "todo_visible": "表示",
        }
