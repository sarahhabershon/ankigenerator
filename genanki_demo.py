import genanki
import csv
import pandas as pd

style = """
.card {
 font-family: arial;
 font-size: 24px;
 text-align: center;
 color: black;
 background-color: white;
}
"""

nz_deck = genanki.Deck(
  1607392319,
  'Deck name')

image_model = genanki.Model(
  1091735104,
  'image card',
  fields=[
    {'name': 'answer'},
    {'name': 'media'},                               
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{media}}',           
      'afmt': '{{FrontSide}}<hr id="answer">{{answer}}',
    },
  ],
  css = style)

text_model = genanki.Model(
  1091735104,
  'Simple Model without Media',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'}, 
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',              
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ],
  css = style)

with open('nz_birds.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        my_note = genanki.Note(
          model=image_model,
          fields=[row['name'], '<img src="' + row['img_name'] + '" />'])
          
        nz_deck.add_note(my_note)
        # print(my_note.fields)

# The text card loop runs twice, to make the card forwards and backwards
with open('nz_text_cards.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        first_note = genanki.Note(
          model=text_model,
          fields=[row['q'], row['a']])
        nz_deck.add_note(first_note)

        second_note = genanki.Note(
          model=text_model,
          fields=[row['a'], row['q']])
        nz_deck.add_note(second_note)
        # print(my_note.fields)

deck_package = genanki.Package(nz_deck)
media_filepaths = "images/" + pd.read_csv('nz_birds.csv')["img_name"]
deck_package.media_files = media_filepaths.tolist()
print(deck_package.media_files)

deck_package.write_to_file('nz.apkg')
