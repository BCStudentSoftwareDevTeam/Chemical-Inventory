from application.models.util import *

class Chemicals (Model):
  chemId          = PrimaryKeyField()
  ## General Information
  name            = CharField(unique = True)
  casNum          = CharField(null = True)
  primaryHazard   = CharField(null = True)
  formula         = CharField(null = True)
  concentration   = CharField(null = True)                   #This field can be left empty
  state           = CharField(null = True)
  structure       = CharField(null = True)       # Organic or Inorganic
  flashPoint      = DecimalField(null = True)
  boilPoint       = DecimalField(null = True)
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
    database = getDB("inventory")

