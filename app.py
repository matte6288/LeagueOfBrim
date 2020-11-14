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
    rank_data=summoner.ranks
    ranked_flex = cass.data.Queue.ranked_flex_fives
    ranked_solo = cass.data.Queue.ranked_solo_fives
    rank = rank_data[cass.data.Queue.ranked_solo_fives]
    rank = str(rank)
    rank = rank.replace("<", "")
    rank = rank.replace(">", "")
    parsed_rank = rank.split(" ")
    tier = parsed_rank[0]
    if (tier == "Challenger"):
        rank_url = "../static/ranked-emblems/Emblem_Challenger.png"
    elif (tier == "Grandmaster"):
        rank_url = "../static/ranked-emblems/Emblem_Grandmaster.png"
    elif (tier == "Master"):
        rank_url = "../static/ranked-emblems/Emblem_Master.png"
    elif (tier == "Diamond"):
        rank_url = "../static/ranked-emblems/Emblem_Diamond.png"
    elif (tier == "Platinum"):
        rank_url = "../static/ranked-emblems/Emblem_Platinum.png"
    elif (tier == "Gold"):
        rank_url = "../static/ranked-emblems/Emblem_Gold.png"
    elif (tier == "Silver"):
        rank_url = "../static/ranked-emblems/Emblem_Silver.png"
    elif (tier == "Bronze"):
        rank_url = "../static/ranked-emblems/Emblem_Bronze.png"
    else:
        rank_url = "../static/ranked-emblems/Emblem_Iron.png"

    icon=summoner.profile_icon.url
    bestChampImage=summoner.champion_masteries.copy().pop(0).champion.skins.copy().pop(0).splash_url
    champUrls=[]
    champMasteriesLevels=[]
    champMasteriesCopy=summoner.champion_masteries.copy()
    for x in range(5):
        champUrls.append(summoner.champion_masteries.pop(0).champion.skins.copy().pop(0).loading_image_url)
        champMasteriesLevels.append(champMasteriesCopy.pop(0).level)
    
    return render_template('summonerRecap.html', name=name, level=level, rank=rank, rankUrl=rank_url, bestChampImage=bestChampImage, icon=icon, champUrls=champUrls, champMasteriesLevels=champMasteriesLevels)


if __name__ == '__main__':
    app.run()
