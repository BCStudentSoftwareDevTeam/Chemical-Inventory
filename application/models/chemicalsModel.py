from application.models.util import *
from application.logic.sortPost import *

class Chemicals (Model):
  chemId          = PrimaryKeyField()
  oldPK           = IntegerField(null = True)
  ## General Information
  name            = CharField(null = True, unique = True)
  casNum          = CharField(null = True)
  primaryHazard   = CharField(null = True)
  formula         = CharField(null = True)
  state           = CharField(null = True)
  structure       = CharField(null = True) # Organic or Inorganic
  flashPoint      = DecimalField(null = True)
  boilPoint       = DecimalField(null = True)
  molecularWeight = DecimalField(null = True)
  storageTemp     = DecimalField(null = True)
  sdsLink         = CharField(null = True)
  description     = CharField(default = "")
  remove          = BooleanField(default = False)
  deleteDate      = DateTimeField(null = True)
  ## NFPA "Fire Diamond"
  healthHazard    = CharField(null = True) # 0-4
  flammable       = CharField(null = True) # 0-4
  reactive        = CharField(null = True) # 0-4
  other           = CharField(null = True)
  ## NFPA "Fire Diamond" DATABASE DOES NOT SUPPORT THESE YET!
  #simpleAsphyxiant= BooleanField(default = False) # Simple Asphyxiant
  #oxidizer        = BooleanField(default = False) # Oxidizer
  waterReactive   = BooleanField(default = False) # Water Reactive
  ## HMIS Color Bar
  hmisHealth      = CharField(null = True) # 0-4
  hmisFlammable   = CharField(null = True) # 0-4
  hmisPhysical    = CharField(null = True) # 0-4
  hmisPPE         = CharField(default = "A") # "A, B, C, D, E, H"
  # Ask the user which pictograms a chemical should have
  hhPict          = BooleanField(default = False) # Health Hazard Pictogram
  flamePict       = BooleanField(default = False) # Flammmable Pictogram
  emPict          = BooleanField(default = False) # Exclamation Mark Pictogram
  gcPict          = BooleanField(default = False) # Gas Cylinder Pictogram
  corrosivePict   = BooleanField(default = False) # Corrosive Pictogram
  expPict         = BooleanField(default = False) # Explosive Pictogram
  oxidizerPict    = BooleanField(default = False) # Oxidizer Pictogram
  oxidizerClass   = CharField(default = '4')      # Only if it is an oxidizer
  envPict         = BooleanField(default = False) # Environmental Hazard
  toxicPict       = BooleanField(default = False) # Acute Toxicity
  peroxideFormer  = BooleanField(default = False)
  pressureFormer  = BooleanField(default = False)

  class Meta:
    database = getDB("inventory", "dynamic")

def createChemical(data):
  """Creates chemical based on input from user."""
  try:
    modelData, extraData = sortPost(data, Chemicals) #Only get relevant data for the current Model
    if modelData['sdsLink'] == None:
      modelData['sdsLink'] = 'https://msdsmanagement.msdsonline.com/af807f3c-b6be-4bd0-873b-f464c8378daa/ebinder/?SearchTerm=%s' %(modelData['name'])
    elif modelData['sdsLink'][0:8] != 'https://' and  modelData['sdsLink'][0:7] != 'http://':
	modelData['sdsLink'] = 'https://' + modelData['sdsLink'] 
    newChem = Chemicals.create(**modelData) #Create instance of Chemical with mapped info in modelData
    return(True, "Chemical Created Successfully!", "list-group-item list-group-item-success", newChem)
  except Exception as e:
    print e
    return(False, "Chemical Could Not Be Created.", "list-group-item list-group-item-danger", None)

def getChemicalOldPK(oldpk):
    try:
        return Chemicals.select().where(Chemicals.oldPK == oldpk).get()
    except Exception as e:
        return e

def getChemical(chemId):
  try:
    return Chemicals.get(Chemicals.chemId == chemId)
  except Exception as e:
    return e

def getChemicals():
  try:
    return Chemicals.select()
  except Exception as e:
    return e
