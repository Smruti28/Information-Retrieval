from bdb import Breakpoint
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from itertools import chain
from collections import Counter


def find_invIndex():
    stop_words = list(stopwords.words('english'))
    stop_words = stop_words+['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', ';', '/', '.', '’s'
                             ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~', ',', '''"''', "'", "'''", 'e.g.',
                             'ex.', 'etc.', 'etc', 'could', 'would', 'should', 'must', 'always']
    tokenized_words = []
    logical_view = []
    d1 = """Demon Slayer: Every Member Of The Hashira, Ranked In Terms Of Strength The
Hashira are humanity's last line of defense against demons. Here's how every single one of
them ranks based on their strength.Demon Slayer is easily one of the most popular anime of
all time, and one need only look at its stellar animation to realize why this is the case.
Ufotable has proven time and time again that their animation work is second to none, with
Demon Slayer setting the bar for what is possible in the realm of animation.RELATED:The
Best Anime To Watch If You Love One PieceThe first season of the anime ended with the
reveal of the powerful Hashira and the role they play in saving humanity from demons.
Viewers who want an in-depth look into the powers of these Hashira need only take a look at
this list to inform themselves.The Hashira are the ultimate Demon Slayers in the series,
serving as masters of their respective styles and making it clear that they're not to be trifled
with. This group of elite Demon Slayers has been through hell and back time and time again,
leading to them steeling their resolves and attaining the highest level of strength possible.
There have been several over the course of the world's history, and among them, some are
more powerful than others. Keeping this in mind, here are all the Hashira — both old and
current — ranked in terms of their overall strength."""
    d2 = """Jigoro Kuwajima, The (Former) Thunder Hashira Jigoro Kuwajima in Demon Slayer In
their current states, the former Hashira won't really be able to hold a candle to the strengths
of their modern counterparts. However, this in no way indicates that these people were weak
in their past — it just means that the new generation has caught up to them and, in some
cases, surpassed tham. After all, no one can really say that Jigoro Kuwajima is an outright
weak person. The fact that he used to be the Thunder Hashira clearly indicates toward his
legacy and the vast horde of power he used to possess. It's only natural that he'd be
overtaken, but he set the groundwork for the Hashira who came after him. Sakonji
Urokodaki, The (Former) Water HashiraSakonji Urokodaki demon slayerJust like Kuwajima, it
would be impossible to write off Urokodaki as an outright weak person. His title as the Water
Hashira of the past means that he was one of the most powerful Demon Slayers around, at
one point. As a master of the technique, he even taught Water Breathing to the current
Water Hashira, Giyu Tomioka. This, in itself, should prove just how vast and amazing Sakonji's
legacy really is. After all, he was able to turn Tanjiro into a powerful practician of Water
Breathing, even though that wasn't his natural style."""
    d3 = """Shinjuro Rengoku, The (Former) Flame Hashira Shinjuro Rengoku in Demon Slayer
The Rengoku family has held the mantle of being the Flame Hashira for generations.
Kyojuro's passion for his craft could be clearly seen in each and every scene featuring him,
and it's a shame that he bid his farewell a bit too soon. Not much is known about Shinjuro
Rengoku, Kyojuro's brother who once held the position of the Flame Hashira. However,
achieving this title is no meager feat in itself. It's clear that Shinjuro had to go through a lot of
trials and tribulations to be recognized at such a high level. Kanae Kocho, The (Former) Insect
Hashira Kanae Kocho in Demon Slayer Just like Shinjuro, a not is known about Kanae's time as
the Insect Hashira. However, it's a given that she was extremely powerful, since everyone
holds her in high regard to this day.The fact that Doma killed her is going to be a source of
great anger for both Shinobu and Kanao. Only time will tell how both warriors will deal with
this battle, once they come face to face with this upper rank demon."""
    d4 = """Tengen Uzui, The Sound Hashira Tengen Uzui in Demon Slayer The Sound Hashira
might have a cool character design, but his power isn't really anything noteworthy. This is
especially true when compared to some of the other Hashira in Demon Slayer who boast
truly impressive powers. As a result, Tengen Uzui has to deal with the moniker of being the
least powerful Hashira around. Of course, that's not the worst thing in the world, as all
Hashira are strong. He's still incredibly powerful and can give any demon a run for their
money. Kyojuro Rengoku, The Flame Hashira Kyojuro in Demon Slayer Rengoku is easily one
of the most lovable Hashira in the series. This is why it's a shame that he succumbed to the
wounds that he suffered in his fight against Akaza. Regardless, the strength that he showed in
this encounter was still incredible to behold. In fact, he could've actually defeated Akaza had
he not been exhausted after saving everyone on the Mugen Train."""
    d5 = """Shinobu Kocho, The Insect Hashira Shinobu Kochu in Demon Slayer Shinobu Kocho is
an effective Hashira whose worthy of being the Insect Hashira. That being said, one has to
admit that she's arguably the weakest Hashira when it comes to pure strength. Demon
Slayer: Every Character's Age, Height, And Birthday However, brawn is not the only way to
determine strength in Demon Slayer. Shinobu's sharp mind coupled with the effective way in
which she wields poisons in battle makes her a force to be reckoned with no matter what.
Obanai Iguro, The Serpent Hashira Obanai Iguro, The Serpent Hashira in Demon SlayerThe
Serpent Hashira hasn't really got the time to shine in the anime. However, manga readers
know precisely how much power Obanai Iguro houses.He's easily one of the strongest
members of the Hashira and can hold his own in a fight against the toughest demons around.
One can only wait and see how the anime will do justice and display the massive strength of
this character."""
    d6 = """Mitsuri Kanroji, The Love Hashira Mitsuri Kanroji, The Love Hashira in Demon Slayer
At a glance, the Love Hashira doesn't really look like a fighter who boasts a ton of raw
strength. However, looks can be very deceptive — Mitsuru Kanroji actually boasts one of the
highest raw strength levels in the Hashira. Most viewers who are underrating the abilities of
this Hashira will be in for a rude awakening when Mitsuri shows precisely how much power
she houses in her body. After all, no mere mortal would be able to rip out Muzan's tentacles
with ease. Muichiro Tokito, The Mist Hashira Muichiro Tokito, The Mist Hashira in Demon
Slayer Muichiro is another Hashira whose true potential is yet to be seen in the anime. That
being said, manga readers aren't worried — given his immense power, it won't take that long
for the Mist Hashira to carve out a stellar reputation amongst the fanbase."""
    d7 = """His mist abilities already sound quite alluring enough as is. Only time will tell whether
these powers will be as amazing to witness in the anime as they were in the manga. Giyu
Tomioka, The Water Hashira Demon Slayer Giyu Out of all the Hashira present in Demon
Slayer, Giyu Tomioka has had the most valuable screentime in the anime as of now. His
powers were a treat to behold, and the manner in which he was able to make short work of
Rui made it extremely clear that the high-level Hashira were a force to be reckoned
with.Given Tanjiro's talents with Water Breathing, one can certainly expect him to spend a
ton of time with Giyu Tomioka as he strives to improve his swordsmanship. Of course,
Tanjiro's real ace in the hole is Hinokami Kagura, and one can only wait and see how this Sun
Breathing develops over the course of the anime."""
    d8 = """Sanemi Shinazugawa, The Wind Hashira Sanemi Shinazugawa, The Wind Hashira in
Demon Slayer Like most of the Hashira in the series, most anime viewers don't really know a
ton about Sanemi Shinazugawa. However, his wild look and demeanor should be indicative
enough of just how powerful this Hashira really is.This ferocity, coupled with the cutting
nature of his Wind Breathing, should make it infinitely clear that Sanemi has a ton of tricks up
his sleeve. Hopefully, the anime will give this ferocious fighter the spotlight he deserves."""
    d9 = """Gyomei Himejima, The Stone Hashira Gyomei Himejima, The Stone Hashira in Demon
Slayer At a glance, Gyomei Himejima might not seem like all that powerful a fighter. The fact
that he carries the unimpressive title of being the Stone Hashira means that most people
won't really take him all that seriously either. However, these people are bound to be
surprised when they find out that Gyomei is actually the strongest Hashira in the entire
group. Suffice to say, his destructive power will be an absolute treat to witness in the series."""
    d10 = """Thunder Breathing is one such technique that Zenitsu has used to great effect in the
series. Of course, Zenitsu is only the master of the first form, but it goes without saying that
the other techniques of Thunder Breathing will also be awe-inspiring to witness in Demon
Slayer. Given how powerful the first form already is, the wait to see the rest of Thunder
Breathing's arsenal is positively agonizing. To satiate the curiosity of fans when it comes to
this breathing style, here are all the techniques from Thunder Breathing and what they
accomplish. The Thunder Breathing style in Demon Slayer is easily one of the most visually
dazzling and spectacular styles. The fact that a comic relief character like Zenitsu sports this
amazing ability makes him an even more dynamic and engaging character. It also indicates
that maybe there's more going on behind the scenes than Zenitsu is letting on... although
that is a conversation best saved for another day. This breathing style has a series of amazing
moves that fans should definitely stay up-to-date with, since it's clear the anime will be
portraying all of them at some point or the other. Considering how powerful this technique
is, this list has been updated to expand on each of the techniques."""
    docs_data = [d1.lower(), d2.lower(), d3.lower(), d4.lower(), d5.lower(), d6.lower(),
                 d7.lower(), d8.lower(), d9.lower(), d10.lower()]
    for word in docs_data:
        tokenized_words.append(word_tokenize(word))
        tokenized_words = list(chain(*tokenized_words))
        tokenized_words = [i.lower() for i in tokenized_words]
        processed_text = []
        for word1 in tokenized_words:
            if word1 not in stop_words and word1.isnumeric() == False and word1.isdecimal() == False and word1.isalpha() and len(word1) >= 3:
                processed_text.append(word1)
        logical_view.append(processed_text)
    cnt_temp = Counter(chain(*logical_view))
    logical_view = [i for i, j in cnt_temp.items() if j >= 1]

    sorted_list = list(sorted(logical_view))
    doc_pos = {index_term: [] for index_term in sorted_list}
    for index_term in sorted_list:
        for i, doc in enumerate(docs_data):
            if doc.find(index_term) >= 0:
                doc_pos[index_term].append((i+1, doc.find(index_term)))
    return [logical_view, sorted_list, doc_pos]


def search_by_invIndex():
    rest = find_invIndex()
    query_type = int(input(
        "\nEnter your Choice:\n1.Single Word Query\n2.Phrase Query(Pattern)\n3.Range Query\n"))
    query = input("Enter Any Query for Searching:\n")
    if query_type == 1:
        result = {}
        words = query.split(' ')
    # print(words)
        for word in words:
            if word.strip('.') in list(rest[2].keys()):
                result[word.strip('.')] = rest[2][word.strip('.')]
    # return {'data': rest[0], 'sorted_data': rest[1], 'inv_index': rest[2], 'result': result}
        return result
    elif query_type == 2:
        result = {}
        for i, j in rest[2].items():
            if i.startswith(query):
                result[i] = rest[2][i]
    # return {'data': rest[0], 'sorted_data': rest[1], 'inv_index': rest[2], 'result': result}
        return result
    elif query_type == 3:
        result = {}
        for word in rest[2].keys():
            if word >= query.split(',')[0] and word <= query.split(',')[1]:
                result[word] = rest[2][word]
    # return {'data': rest[0], 'sorted_data': rest[1], 'inv_index': rest[2], 'result': result}
        print(result)
        return result
    else:
        return "Invalid Query Type Selected."


res = find_invIndex()
print("The logical view of documents are as follow:")
for i in range(len(res[0])):
    print(res[0][i], end=" ")
print("\n")
print("The Sorted List of Logical view as follow:")
for i in range(len(res[1])):
    print(res[1][i], end=" ")
print("\n")
print("The Inverted Index for given documents is as follow:")
print(res[2])
print("\n")
while (1):
    res1 = search_by_invIndex()
    if res1 == "Invalid Query Type Selected.":
        print("You Have Selected Invalid Query Type")
    else:
        print("The Result of your Search Query is as follow:")
    for i in res1.items():
        print(i, end=" ")
    print()
    bsk = int(input("For continue Enter 1,For exit enter 0:"))
    if bsk == 0:
        break
