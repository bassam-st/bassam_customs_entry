from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Bassam Customs Entry (A4 mm)")

# إعداد مجلدات الملفات الثابتة والقوالب
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# الصفحة الرئيسية (واجهة الإدخال)
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("entry.html", {"request": request})

# مسار الطباعة
@app.post("/print", response_class=HTMLResponse)
async def print_form(request: Request):
    form = await request.form()
    data = {k: form.get(k, "") for k in form.keys()}
    # نرسل البيانات إلى صفحة الطباعة بالمليمتر
    data["items"] = [{} for _ in range(10)]  # جدول البضائع (فارغ الآن)
    return templates.TemplateResponse("customs_a4.html", {"request": request, "d": data})
