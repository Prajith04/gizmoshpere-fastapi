from fastapi import FastAPI, Request, Form, Depends, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from db import engine, SessionLocal, Base, ContactForm as DBContactForm,BuyForm
app=FastAPI()
templates=Jinja2Templates(directory="templates")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
async def home(request:Request):
    return templates.TemplateResponse("home.html",context={"request":request})
@app.get('/blog')
async def home(request:Request):
    return templates.TemplateResponse("blog.html",context={"request":request})
@app.get('/about-us')
async def home(request:Request):
    return templates.TemplateResponse("aboutus.html",context={"request":request})
@app.get('/contact-us')
async def home(request:Request):
    return templates.TemplateResponse("contactus.html",context={"request":request})
@app.get('/smartphones')
async def home(request:Request):
    return templates.TemplateResponse("smartphones.html",context={"request":request})
@app.get('/wearables')
async def home(request:Request):
    return templates.TemplateResponse("wearables.html",context={"request":request})
@app.get('/laptops')
async def home(request:Request):
    return templates.TemplateResponse("laptops.html",context={"request":request})
@app.get('/blog1')
async def home(request:Request):
    return templates.TemplateResponse("blog1.html",context={"request":request})
@app.get('/blog2')
async def home(request:Request):
    return templates.TemplateResponse("blog2.html",context={"request":request})

@app.post("/contact", response_class=HTMLResponse)
async def submit_contact(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...), db: Session = Depends(get_db)):
    # Handle form submission logic here
    contact_form = DBContactForm(name=name, email=email, message=message)
    db.add(contact_form)
    db.commit()
    db.refresh(contact_form)
    
    success_message = "Your message has been sent successfully!"
    return templates.TemplateResponse("contactus.html", {"request": request, "message": success_message})
@app.get("/buy", response_class=HTMLResponse)
async def buy(request: Request, product_name: str = Query(...), price: str = Query(...)):
    # Handle the buying logic here
    return templates.TemplateResponse("Buy.html",{"request": request,"product_name": product_name, "price": price})
@app.post("/buy", response_class=HTMLResponse)
async def process_buy(request: Request, product_name: str = Form(...), email: str = Form(...), price: int = Form(...), db: Session = Depends(get_db)):
    # Process the form data (store in database, send email, etc.)
    buy_form = BuyForm(product_name=product_name, email=email, price=price)
    db.add(buy_form)
    db.commit()
    db.refresh(buy_form)
    success_message = f"Thank you for buying"
    return templates.TemplateResponse("buy.html", {"request": request, "message": success_message})