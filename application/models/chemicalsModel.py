from application.models.util import *

class Chemicals (Model):
  chemId          = PrimaryKeyField()
  ## General Information
  name            = CharField(unique = True)
  casNum          = CharField(null = False)
  primaryHazard   = CharField(null = False)
  formula         = CharField(null = False)
  concentration   = CharField(null = True)                   #This field can be left empty
  state           = CharField(null = False)
  structure       = CharField(null = False)       # Organic or Inorganic
  flashPoint      = DecimalField(null = True)
  boilPoint       = DecimalField(null = True)
  storageTemp     = DecimalField(null = True)
  sdsLink         = CharField(null = True)
  description     = CharField(default = "")
  ## NFPA "Fire Diamond"
  healthHazard    = CharField(null = False) # 0-4
  flammable       = CharField(null = False) # 0-4
  reactive        = CharField(null = False) # 0-4
  other           = CharField(null = False) # Ask Leslie if they use any non-standard symbols
  ## NFPA "Fire Diamond" DATABASE DOES NOT SUPPORT THESE YET!
  #simpleAsphyxiant= BooleanField(default = False) # Simple Asphyxiant
  #oxidizer        = BooleanField(default = False) # Oxidizer
  waterReactive   = BooleanField(default = False) # Water Reactive
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

