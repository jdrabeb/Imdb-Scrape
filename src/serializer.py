import csv
import json

def create_csv(games):
    with open('csv/games.csv', mode='w') as csv_file:
        fieldnames = ['title', 'link', 'image', 'date', 'genre', 'rating',
               'description', 'votes']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for game in games:
            writer.writerow({'title': game.get_title()})
            writer.writerow({'link': game.get_link()})
            writer.writerow({'image': game.get_image()})
            writer.writerow({'date': game.get_date()})
            writer.writerow({'genre': game.get_genre()})
            writer.writerow({'rating': game.get_rating()})
            writer.writerow({'description': game.get_description()})
            writer.writerow({'votes': game.get_votes()})

def create_json(games):
    with open('json/games.json', 'w') as json_file:
        for game in games:
            data = json.dumps(game.__dict__)
            json.dump(data, json_file)

