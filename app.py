from flask import *
import cassiopeia as cass



cass.set_riot_api_key("RGAPI-19beacd2-3197-446b-9246-562628b747ff")
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
    if not summoner.exists:
        return render_template('summonerSearchPage.html')
    name=sumName
    level=summoner.level
    rank_data=summoner.ranks
    if cass.data.Queue.ranked_solo_fives in rank_data:
        solo_rank = rank_data[cass.data.Queue.ranked_solo_fives]
        solo_rank = str(solo_rank)
        solo_rank = solo_rank.replace("<", "")
        solo_rank = solo_rank.replace(">", "")
        solo_parsed_rank = solo_rank.split(" ")
        solo_tier = solo_parsed_rank[0]
        if (solo_tier == "Challenger"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Challenger.png"
        elif (solo_tier == "Grandmaster"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Grandmaster.png"
        elif (solo_tier == "Master"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Master.png"
        elif (solo_tier == "Diamond"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Diamond.png"
        elif (solo_tier == "Platinum"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Platinum.png"
        elif (solo_tier == "Gold"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Gold.png"
        elif (solo_tier == "Silver"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Silver.png"
        elif (solo_tier == "Bronze"):
            solo_rank_url = "../static/ranked-emblems/Emblem_Bronze.png"
        else:
            solo_rank_url = "../static/ranked-emblems/Emblem_Iron.png"
    else:
        solo_rank = "Unranked"
        solo_rank_url = "../static/ranked-emblems/unranked.png"

    if cass.data.Queue.ranked_flex_fives in rank_data:
        flex_rank = rank_data[cass.data.Queue.ranked_flex_fives]
        flex_rank = str(flex_rank)
        flex_rank = flex_rank.replace("<", "")
        flex_rank = flex_rank.replace(">", "")
        flex_parsed_rank = flex_rank.split(" ")
        flex_tier = flex_parsed_rank[0]
        if (flex_tier == "Challenger"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Challenger.png"
        elif (flex_tier == "Grandmaster"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Grandmaster.png"
        elif (flex_tier == "Master"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Master.png"
        elif (flex_tier == "Diamond"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Diamond.png"
        elif (flex_tier == "Platinum"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Platinum.png"
        elif (flex_tier == "Gold"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Gold.png"
        elif (flex_tier == "Silver"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Silver.png"
        elif (flex_tier == "Bronze"):
            flex_rank_url = "../static/ranked-emblems/Emblem_Bronze.png"
        else:
            flex_rank_url = "../static/ranked-emblems/Emblem_Iron.png"
    else:
        flex_rank = "Unranked"
        flex_rank_url = "../static/ranked-emblems/unranked.png"

    icon=summoner.profile_icon.url

    champFullArtUrls=[]
    champSplashUrls=[]
    champMasteriesLevels=[]
    champMasteriesPoints=[]
    champMasteryImageURLS=[]
    champMasteryNames=[]
    champMasteriesCopy=summoner.champion_masteries.copy()
    champMasteriesCopy2=summoner.champion_masteries.copy()
    champMasteriesCopy3=summoner.champion_masteries.copy()
    champMasteriesCopy4=summoner.champion_masteries.copy()
    champMasteriesCopy5=summoner.champion_masteries.copy()

    for x in range(5):
        champSplashUrls.append(champMasteriesCopy.pop(0).champion.skins.copy().pop(0).loading_image_url)
        champFullArtUrls.append(champMasteriesCopy2.pop(0).champion.skins.copy().pop(0).splash_url)
        champMasteriesLevels.append(champMasteriesCopy3.pop(0).level)
        champMasteriesPoints.append(champMasteriesCopy4.pop(0).points)
        champMasteryNames.append(champMasteriesCopy5.pop(0).champion.name)
        champMasteryImageURLS.append("../static/champion-mastery-icons/mastery-1"+str(champMasteriesLevels[x])+".png")

    
    champMasteriesCopy=summoner.champion_masteries.copy()
    champMasteriesCopy2=summoner.champion_masteries.copy()
    champMasteriesCopy3=summoner.champion_masteries.copy()
    champMasteriesCopy4=summoner.champion_masteries.copy()
    return render_template('summonerRecap.html', name=name, level=level, soloRank=solo_rank, soloRankUrl=solo_rank_url, \
        icon=icon, champFullArtUrls=champFullArtUrls, champSplashUrls=champSplashUrls, champMasteryImageURLS=champMasteryImageURLS, \
        champMasteriesPoints=champMasteriesPoints, champMasteryNames=champMasteryNames, flexRank=flex_rank, flexRankUrl=flex_rank_url)



if __name__ == '__main__':
    app.run()
