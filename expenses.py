import csv

class Category:
    name = 'Unspecifeid'
    words = []
    total_cost = 0
    lines = []
    def __init__(self, name, words):
        self.name = name
        self.words = words
        self.lines = []


def AddToCategory(category, useful_line, price):
    category.total_cost += price
    category.lines.append('$' + str(price) + ' ' + useful_line)


grocery = Category('Grocery', ['safeway', 'costco', 'fred meyer', 'qfc',
  'QUALITY F 211', 'WHOLEFDS', 'TRADER JOE', 'QUALITY FOOD', 'FRESH', 'WALMART',
  'METROPOLITAN'])
car = Category('Car', ['SHELL', 'CHEVRON', 'AN FORD BELLEVUE', 'car loan',
  'GOOD2GO', 'VEHICLE', 'ARCO'])
house = Category('House', ['9324404095', 'CITYOFKIRKLAND 123 5TH AVE',
  'FRONTPOINT', 'Assn dues', 'CITY-KIRKLAND'])
cafes = Category('Cafes', ['QDOBA', 'ALANYA', 'COPPERSTONE', 'HOMEGROWN',
  'ARIANA', 'SUKHO THAI', 'ACROPOLIS PIZZA', 'THE ORIGINAL PANCAKE', 'THE FRENCH BAKERY', 
  'SARDUCCI', 'WILDE ROVER', 'RISTORANTE', 'TAVERN HALL', 'CACTUS',
  'KANISHKA', 'THE GUILT TRIP', 'EL TOREADOR', 'CAFE', 'LECOSHO', 'SIMILAN THAI', 
  'GARLIC CRUSH', 'CHRYSALIS INN RESTAURA', 'RESTAURANT', 'NIBBANA',
  'ETHIOPIAN CUISINE', 'PUFFIN ON', 'PANERA', 'HANUMAN', 'BAI TONG',
  'MEDITERRANEAN', 'STARBUCKS', 'LIZZYKATE', 'DOUGH ZONE', 'DOORDASH', 'CUISI',
  'OLIVE', 'PEACH', 'MERCURYS', 'MEXICAN', 'TAPIOCA', 'DUMPLING', 'SMOOTHIE',
  'TASTE', 'BITES', 'EGG AND', 'CHEESE', 'ABBEY', 'GRILL', 'COFFEE', 'PIROSHKY',
  'PANCAKE', 'RED ROBIN', 'PANIER', 'CHAINLINE', 'DELI', 'FALAFE', 'RAMEN',
  'VOLTERRA', 'VILLAGE SQUARE', 'KITANDA', 'PINTXO', 'BEECHER', 'CASA RIC',
  'PAPA JOHN', 'LA FONTANA', 'GORDON BIERSCH', 'REVOLVE FOOD'])
phone = Category('Phone, Internet', ['AT+T*BILL', 'COMCAST', 'NETFLIX.COM',
  'T-MOBILE', 'TMOBILE', 'FRONTIER', 'VZWR'])
energy = Category('Energy', ['PUGET SOUND ENER'])
amazon = Category('Amazon', ['AMAZON'])
daycare = Category('Daycare', ['Check #'])
# Перевод с одного аккаунта на свой же другой.
ignore_category = Category('Ignore', ['9321085624', '9330223778', '9324247098',
  '9324089359', '9332519231', 'LYFT', 'JAMAICA BAY INN'])

other_category = Category('Other', [])


def addToDict(dic, month, amount):
   if month not in dic: dic[month] = 0
   dic[month] = dic[month] + amount

def printForSun(dic):
  for key, value in dic.items():
    print(key + ": " + str(value))

def printLargeLoss(expense, large):
  print ('LARGE')
  for key, value in large.items():
    print(key + ": " + str(value))
    print(key + ": " + str(value / expense[key]))


def exp(fileName):
  with open(fileName, 'rt', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    first = True
    for row in spamreader:
      if first:
        first = False
        continue

      text = row[7]
      amount = float(row[4])

      date_split = row[1].split('/')
      month = date_split[0] + '/' + date_split[2]

      if amount > 0: continue

      category_found = False
      ignore = False

      for category in [grocery, car, house, cafes, phone, energy, amazon, daycare]:
        for word in category.words:
            if(word.lower() in text.lower()):
                category_found = True
                AddToCategory(category, text, amount)
                break
        if(category_found): break
      for word in ignore_category.words:
        if(word.lower() in text.lower()):
          AddToCategory(ignore_category, text, amount)
          ignore = True
      if (ignore): continue
      if(not category_found): AddToCategory(other_category, text, amount)

exp("AndreyApr.csv")
exp("SandraApr.csv")

for category in [grocery, car, house, cafes, phone, energy, amazon,
    other_category, daycare]:
    print('---------------------------' + category.name.upper() + '----------------------------------------------')
    for line in category.lines:
        print(line, end='\n')
    print('\n\n\n\n')

print('---------------------------IGNORE---------------------------------------------')
for line in ignore_category.lines:
    print(line, end='\n')
print('\n\n\n\n')

total = 0
for category in [grocery, car, house, cafes, phone, energy, amazon, other_category]:
    print(category.name + ': $' + str(category.total_cost))
    total += category.total_cost

print('TOTAL: $' + str(total))
