
""" evento del timeline generator """

class Event:
    
    date_default="0000-00-00"
    date=""
    datetime=""
    title=""
    description=""
    link=""
    
    
    def __init__(self,date,title,description,link_optional="") -> None:
        self.date=self.date_default if date=="" else date
        self.link="#" if link_optional=="" else link_optional
        self.title=title
        self.description=description
        
        self.date=self.date.strip()
        self.link=self.link.strip()
        self.title=self.title.strip()
        self.description=self.description.strip()
    
    def get_arg_date_format(self):
        date=self.date.split("-")
        hours=date[len(date)-1].split(" ")
        hours_final="" if len(hours)==1 else hours[1]
        return hours[0]+"/"+date[1]+"/"+date[0]+" - "+hours_final