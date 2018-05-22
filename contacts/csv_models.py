from adaptor.model import CsvModel
from . import models.Contact

class ContactCsv(CsvModel):
	class Meta:
        delimiter = ","
        dbModel = Contact
