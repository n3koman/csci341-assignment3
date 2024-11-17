from app import db

class Country(db.Model):
    __tablename__ = 'country'

    cname = db.Column(db.String(50), primary_key=True)
    population = db.Column(db.BigInteger, nullable=False)


class Users(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(60), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(40), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    cname = db.Column(db.String(50), db.ForeignKey('country.cname'), nullable=False)


class Patients(db.Model):
    __tablename__ = 'patients'

    email = db.Column(db.String(60), db.ForeignKey('users.email'), primary_key=True)


class DiseaseType(db.Model):
    __tablename__ = 'disease_type'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140), nullable=False)


class Disease(db.Model):
    __tablename__ = 'disease'

    disease_code = db.Column(db.String(50), primary_key=True)
    pathogen = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(140), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('disease_type.id'), nullable=False)


class Discover(db.Model):
    __tablename__ = 'discover'

    cname = db.Column(db.String(50), db.ForeignKey('country.cname'), primary_key=True)
    disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code'), primary_key=True)
    first_enc_date = db.Column(db.Date, nullable=False)


class PatientDisease(db.Model):
    __tablename__ = 'patient_disease'

    email = db.Column(db.String(60), db.ForeignKey('users.email'), primary_key=True)
    disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code'), primary_key=True)


class PublicServant(db.Model):
    __tablename__ = 'public_servant'

    email = db.Column(db.String(60), db.ForeignKey('users.email'), primary_key=True)
    department = db.Column(db.String(50), nullable=False)


class Doctor(db.Model):
    __tablename__ = 'doctor'

    email = db.Column(db.String(60), db.ForeignKey('users.email'), primary_key=True)
    degree = db.Column(db.String(20), nullable=False)


class Specialize(db.Model):
    __tablename__ = 'specialize'

    id = db.Column(db.Integer, db.ForeignKey('disease_type.id'), primary_key=True)
    email = db.Column(db.String(60), db.ForeignKey('doctor.email'), primary_key=True)


class Record(db.Model):
    __tablename__ = 'record'

    email = db.Column(db.String(60), db.ForeignKey('public_servant.email'), primary_key=True)
    cname = db.Column(db.String(50), db.ForeignKey('country.cname'), primary_key=True)
    disease_code = db.Column(db.String(50), db.ForeignKey('disease.disease_code'), primary_key=True)
    total_deaths = db.Column(db.Integer, nullable=False)
    total_patients = db.Column(db.Integer, nullable=False)
