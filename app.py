from flask import *
import cassiopeia as cass



cass.set_riot_api_key("RGAPI-d68fd3e9-fad3-451e-a5b9-689c8e061921")
cass.set_default_region("NA")

app = Flask(__name__)
app.static_folder='static'


@app.route('/')
def default():
    return redirect(url_for('summonerSearchPage'))

@app.route('/summonerSearchPage', methods=['GET', 'POST'])
def summonerSearchPage():
    if request.method =="POST":
        summonerName=request.form["SummonerName"]
        return redirect(url_for('summonerRecap', sumName=summonerName))
    else:
        return render_template('summonerSearchPage.html')

@app.route("/<sumName>")
def summonerRecap(sumName):
    summoner=cass.get_summoner(name=sumName)
    name=sumName
    level=summoner.level
    rank=summoner.ranks
    icon=summoner.profile_icon.url
    bestChampImage=summoner.champion_masteries.copy().pop(0).champion.skins.copy().pop(0).splash_url
    champUrls=[]
    champMasteriesLevels=[]
    champMasteriesCopy=summoner.champion_masteries.copy()
    for x in range(5):
        champUrls.append(summoner.champion_masteries.pop(0).champion.skins.copy().pop(0).loading_image_url)
        champMasteriesLevels.append(champMasteriesCopy.pop(0).level)
    return render_template('summonerRecap.html', name=name, level=level, rank=rank, bestChampImage=bestChampImage, icon=icon, champUrls=champUrls, champMasteriesLevels=champMasteriesLevels)


if __name__ == '__main__':
    app.run()
