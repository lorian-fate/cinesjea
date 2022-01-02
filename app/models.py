from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_


from app import db
import datetime
import calendar

class MyFilms(db.Model):
    __tablename__ = "films"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    film_title = db.Column(db.String(250), unique=True, nullable=False)
    film_category = db.Column(db.String(250), nullable=False)
    film_title_slug = db.Column(db.String(250), unique=True, nullable=False)
    film_synopsis = db.Column(db.Text)
    film_image = db.Column(db.String, nullable=False)
    film_opening = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    film_proyection = db.relationship(
        'Proyections', backref='films', lazy=True, 
        cascade='all, delete-orphan', order_by='asc(Proyections.created)')

    def __repr__(self):
        return f"<Film {self.film_title}>"

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.film_title_slug:
            self.film_title_slug = slugify(self.film_title)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                db.session.rollback()
                db.session.add(self)
                count += 1
                self.film_title_slug = f"{slugify(self.film_title)}{count}"

    
    @staticmethod
    def get_all():
        return MyFilms.query.all()
    
    @staticmethod
    def get_by_id(id):
        return MyFilms.query.get(id)
    
    @staticmethod
    def get_by_filmname(film_title):
        return MyFilms.query.filter_by(film_title=film_title).first()
    
    @staticmethod
    def get_nex_opening():
        formato = '%Y-%m-%d'
        current_day = datetime.datetime.today().strftime(formato)
        myFilms = MyFilms.query.filter(MyFilms.film_opening >= str(current_day)).all()
        return myFilms
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    @staticmethod
    def all_paginated(page=1, per_page=20):
        return MyFilms.query.order_by(MyFilms.created.asc()).\
            paginate(page=page, per_page=per_page, error_out=False)




class MyRooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rooms_name = db.Column(db.String(250), unique=True, nullable=False)
    seatss_number = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return MyRooms.query.all()
    
    @staticmethod
    def get_by_roomname(rooms_name):
        return MyRooms.query.filter_by(rooms_name=rooms_name).first()




class MyTicket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    film_name = db.Column(db.String(250), nullable=False)
    room_number = db.Column(db.String(250), nullable=False)
    proyection_time = db.Column(db.String(250), nullable=False)
    proyection_date = db.Column(db.String(250), nullable=False)
    seatss_number = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return MyTicket.query.all()
    
    @staticmethod
    def verifyTicket(film_name, room, p_time, p_date, s_number):
        my_Query = MyTicket.query.filter_by(film_name=film_name).all()
        my_It = []
        for x in my_Query:
            if (x.proyection_time == str(p_time)) and (x.proyection_date == str(p_date) and (x.seatss_number == s_number)):
                my_It.append(x)
        if len(my_It) == 0:
            return None
        else:
            return my_It[0]

    @staticmethod
    def get_by_user_id(user_id):
        return MyTicket.query.filter_by(user_id=user_id).all()




class Proyections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('films.id', ondelete='CASCADE'), nullable=False)
    film_title = db.Column(db.String(250), nullable=False)
    room_number = db.Column(db.String(250), nullable=False)
    proyection_time = db.Column(db.String(250), nullable=False)
    proyection_date = db.Column(db.String(250), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    @staticmethod
    def get_by_id(id):
        return Proyections.query.get(id)

    @staticmethod
    def get_all():
        my_Query = Proyections.query.all()
        myListP = []
        myListF = []
        for x in my_Query:
            if x.film_title not in myListF:
                myListF.append(x.film_title)
                myListP.append(x)
        return myListP
    
    @staticmethod
    def get_all_pro(id):
        current_day = datetime.datetime.today()
        current_day = current_day - datetime.timedelta(days=1)
        my_Query = Proyections.query.filter(Proyections.proyection_date >= str(current_day))
        myListF = [x for x in my_Query if x.film_id == id]
        return myListF
    

    @staticmethod
    def verify_Date(date_proy):
        fdate = str(date_proy).split('-')
        film_date = datetime.datetime(int(fdate[0]), int(fdate[1]), int(fdate[2]), 0, 0, 0)
        current_day = datetime.datetime.now()
        day_diference = film_date - current_day
        if day_diference.days > 2:
            return True
        else:
            return False
    

    @staticmethod
    def verify_Proyection(f_title, f_date, f_time):
        my_Q = Proyections.query.filter_by(film_title=f_title).all()
        my_It = []
        for x in my_Q:
            if (x.proyection_time == str(f_time)) and (x.proyection_date == str(f_date)):
                my_It.append(x)
        if len(my_It) == 0:
            return None
        else:
            return my_It[0]
    

    @staticmethod
    def verify_opening(film_obj, p_date):
        f_opening = str(film_obj.film_opening).split('-')
        date_opening = datetime.date(int(f_opening[0]), int(f_opening[1]), int(f_opening[2]))
        if p_date > date_opening:
            return True
        else:
            return False
        

    @staticmethod
    def get_by_week():
        weekdays = 6
        current_day = datetime.datetime.today()
        weekd = datetime.datetime.today().weekday()
        dDD = weekdays - weekd
        weekdate = current_day + datetime.timedelta(days=dDD)
        current_day = current_day - datetime.timedelta(days=1)
        my_Query = Proyections.query.filter(Proyections.proyection_date >= str(current_day)).\
                                filter(Proyections.proyection_date <= str(weekdate))
        myListP = []
        myListF = []
        for x in my_Query:
            if x.film_title not in myListF:
                myListF.append(x.film_title)
                myListP.append(x)
        return myListP
    
    @staticmethod
    def get_by_week_from_film(id):
        weekdays = 6
        current_day = datetime.datetime.today()
        weekd = datetime.datetime.today().weekday()
        dDD = weekdays - weekd
        weekdate = current_day + datetime.timedelta(days=dDD)
        current_day = current_day - datetime.timedelta(days=1)
        my_Query = Proyections.query.filter(Proyections.proyection_date >= str(current_day)).\
                                filter(Proyections.proyection_date <= str(weekdate))
        myListF = [x for x in my_Query if x.film_id == id]
        return myListF


    @staticmethod
    def get_by_month():
        formato = '%Y-%m-%d'
        current_day = datetime.datetime.today()
        lastDay = calendar.monthrange(current_day.year, current_day.month)[1]
        it_D = str(current_day).split('-')
        last_date = datetime.datetime(int(it_D[0]), int(it_D[1]), int(lastDay))
        current_day = current_day - datetime.timedelta(days=1)
        my_Query = Proyections.query.filter(Proyections.proyection_date >= str(current_day)).\
                                filter(Proyections.proyection_date <= str(last_date))
        
        myListP = []
        myListF = []
        for x in my_Query:
            if x.film_title not in myListF:
                myListF.append(x.film_title)
                myListP.append(x)
        return myListP

    @staticmethod
    def get_by_month_from_film(id):
        formato = '%Y-%m-%d'
        current_day = datetime.datetime.today()
        lastDay = calendar.monthrange(current_day.year, current_day.month)[1]
        it_D = str(current_day).split('-')
        last_date = datetime.datetime(int(it_D[0]), int(it_D[1]), int(lastDay))
        current_day = current_day - datetime.timedelta(days=1)
        my_Query = Proyections.query.filter(Proyections.proyection_date >= str(current_day)).\
                                filter(Proyections.proyection_date <= str(last_date))
        
        myListF = []
        for x in my_Query:
            if x.film_id == id:
                myListF.append(x)
        return myListF


    @staticmethod
    def get_next_ten_days():
        current_day = datetime.datetime.today()
        next_ten_da = current_day + datetime.timedelta(days=10)
        current_day = current_day - datetime.timedelta(days=1)
        my_Query = Proyections.query.filter(Proyections.proyection_date >= str(current_day)).\
                                filter(Proyections.proyection_date <= str(next_ten_da))
        myListP = []
        myListF = []
        for x in my_Query:
            if x.film_title not in myListF:
                myListF.append(x.film_title)
                myListP.append(x)
        return myListP
    
    @staticmethod
    def get_next_ten_days_from_film(id):
        current_day = datetime.datetime.today()
        next_ten_da = current_day + datetime.timedelta(days=10)
        current_day = current_day - datetime.timedelta(days=1)
        my_Query = Proyections.query.filter(Proyections.proyection_date >= str(current_day)).\
                                filter(Proyections.proyection_date <= str(next_ten_da))
        myListF = [x for x in my_Query if x.film_id == id]
        return myListF
    

    @staticmethod
    def get_proyections_by_film_id(f_id):
        return Proyections.query.filter_by(film_id=f_id).all()
        
    