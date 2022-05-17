def createacc()->str:
    text=  """CREATE TABLE IF NOT EXISTS public.accounts(
    user_id integer NOT NULL PRIMARY KEY UNIQUE,
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    email character varying(255)  NOT NULL UNIQUE,
    created_on timestamp without time zone NOT NULL,
    last_login timestamp without time zone)"""
    return text

def createcars()->str:
    text=  """CREATE TABLE IF NOT EXISTS public.cars(
    car_id integer NOT NULL PRIMARY KEY,
    mark character varying(50)  NOT NULL,
    model character varying(50) NOT NULL,
    color character varying(50) NOT NULL,
    horsepower integer NOT NULL,
    working boolean)"""
    return text



def createclient()->str:
    text=  """    CREATE TABLE IF NOT EXISTS public.client(
    cilen_id integer NOT NULL  PRIMARY KEY,
    name character varying(50)  NOT NULL,
    lastname character varying(50) NOT NULL,
    age integer NOT NULL,
    adress character varying(50) NOT NULL UNIQUE);"""
    return text

def createrent()->str:
    text=  """ CREATE TABLE IF NOT EXISTS public.rent(
    rent_id integer NOT NULL PRIMARY KEY ,
    startdate timestamp without time zone NOT NULL,
    enddate timestamp without time zone NOT NULL);"""
    return text