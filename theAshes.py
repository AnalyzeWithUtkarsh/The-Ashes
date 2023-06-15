import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import streamlit as st
from PIL import Image
import plotly.express as px
import Helper

ashes = pd.read_excel("D:\\III YEAR ASSIGNMENTS\\Kaggle Datasets\\Random Datasets\\Ashes.xlsx", sheet_name=None)
results = ashes.get('Results')
batters = ashes.get('Most Runs')
bowlers = ashes.get('Most Wickets')

Helper.img1()

user_menu = st.sidebar.radio(
    'Select an option',
    ('The Ashes Dashboard', 'Bowlers Analysis', 'Batters Analysis')
)

if user_menu == 'The Ashes Dashboard':
    col1, col2, col3, col4 = st.columns(4)

    with col3:
        img = Image.open('e.png')
        st.image(img)
    with col1:
        st.title('THE ASHES')

    with col2:

        img = Image.open('aus.png')
        st.image(img)

    with col4:
        st.title('')

    st.title('')
    st.header('THE TERM "ASHES" WAS FIRST USED AFTER ENGLAND LOST TO AUSTRALIA '
              '- FOR THE FIRST TIME ON HOME SOIL - AT THE OVAL ON 29TH AUGUST 1882')

    st.header('')

    st.write('A day later, the Sporting Times carried a mock obituary of English cricket which concluded that:'
             '"The body will be cremated and the ashes taken to Australia". The concept caught the imagination of the '
             'sporting public.'
             'A few weeks later, an English team, captained by the Hon Ivo Bligh [later Lord Darnley], set off to '
             'tour Australia,'
             'with Bligh vowing to return with "the ashes"; his Australian counterpart, WL Murdoch, similarly vowed '
             'to defend them.'
             'As well as playing three scheduled matches against the Australian national side, Bligh and the amateur '
             'players in'
             'his team participated in many social matches. It was after one such match, at the Rupertswood Estate '
             'outside'
             'Melbourne on Christmas Eve 1882, that Bligh was given the small terracotta urn as a symbol of the ashes '
             'that he had travelled'
             'to Australia to regain. On the same occasion, he met his future wife - Florence Morphy - who was the '
             'companion to'
             'Lady Janet Clarke, mistress of Rupertswood, and governess to the Clark children. In February 1884, '
             'Bligh married Florence.'
             'Shortly afterwards, they returned to England, taking the urn - which Bligh always regarded as a '
             'personal gift - with them.'
             'It stayed on the mantelpiece at the Bligh family home - Cobham Hall, near Rochester in Kent - until Bligh'
             'died, 43 years later.'
             'At his request, Florence bequeathed the urn to MCC.')

    st.title('')
    st.header('')
    st.title('')
    series_win = Helper.most_series_win(results)

    st.header('Series Split')
    st.title('')
    chart = (
        alt.Chart(series_win)
        .mark_bar()
        .encode(
            x="Winner",
            y="Series Won",
            color='Winner'
        )
        .interactive()
    )
    st.altair_chart(chart, use_container_width=True)

    st.title("")
    st.title('')
    st.header('Matches won by both Teams')
    st.title('')
    col1, col2, col3 = st.columns(3)
    with col1:
        aus = results['Australia'].sum()
        st.header('Australia')
        st.title(aus)

    with col2:
        eng = results['England'].sum()
        st.header("England")
        st.title(eng)

    with col3:
        draw = results['Draw'].sum()
        st.header('Draw')
        st.title(draw)

    st.title('')
    st.title('')
    st.title('Results of last 5 Ashes Series')
    st.title('')
    D = results.tail().reset_index()
    D = D[['Series', 'Host ', 'Season', 'Winner', 'Australia', 'England', 'Draw', 'Margin']]
    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(D)

    st.title('')
    st.title('')
    st.title('The Clean Sweeps')
    st.title('')
    col1, col2 = st.columns([1, 2])
    aus = results[(results['England'] == 0) & (results['Draw'] == 0)]
    a = aus.shape[0]
    with col1:
        st.title('Australia')
        st.title(a)

    eng = results[(results['Australia'] == 0) & (results['Draw'] == 0)]
    e = eng.shape[0]

    st.title('')

    aus = results[(results['England'] == 0) & (results['Draw'] == 0)]
    eng = results[(results['Australia'] == 0) & (results['Draw'] == 0)]
    with col2:
        st.title('')
        st.table(aus)

    col1, col2 = st.columns([1, 2])
    with col1:
        st.title('England')
        st.title(e)

    with col2:
        st.title('')
        st.table(eng)


elif user_menu == 'Bowlers Analysis':

    st.header('The Greats of The Game')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        i2 = Image.open('bowler.png')
        st.image(i2, caption='Shane Warne', width=250)

    with col2:
        i3 = Image.open('g.png')
        st.image(i3, caption='Glenn McGrath', width=250)
    with col3:
        i4 = Image.open('an.png')
        st.image(i4, width=250, caption='James Anderson')
    with col4:
        i5 = Image.open('i.png')
        st.image(i5, width=250, caption='Sir Ian Bothom')

    st.header('Wickets Taken & Bowling Averages of both Countries')
    st.title('')
    col1, col2, col3, col4 = st.columns(4)
    e = Helper.wkts_by_country(bowlers)
    r = Helper.country_avg(bowlers)
    with col1:
        b1 = e['Wkts'][0]
        st.header('Australia')
        st.header(b1)

    with col3:
        b2 = e['Wkts'][1]
        st.header('England')
        st.header(b2)

    with col2:
        a = round((r['Runs'][0] / e['Wkts'][0]), 2)
        st.title('')
        st.title('')
        st.header(a)

    with col4:
        q1 = round((r['Runs'][1] / e['Wkts'][1]), 2)
        st.title('')
        st.title('')
        st.header(q1)

    st.title('')
    st.title('')

    st.header('Top 5 Spells in The Ashes History ')
    st.title('')
    spells = Helper.top_spells(bowlers)
    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(spells)
    st.title('')
    st.title('')
    t = Helper.most_successful_bowlers(bowlers)
    st.header('Top Wicket Takers in The Ashes History')
    st.title('')
    chart = alt.Chart(t).mark_bar().encode(y='Player', x='Wkts', color='Country'). \
        properties(height=300, width=700)

    fig, ax = plt.subplots()
    a = t.plot.barh()
    st.altair_chart(chart)

    # -------------------------------------------------------------------------
    st.title('')
    st.title('')
    four_or_more_wkts = Helper.four_or_more_wkts_per_innings(bowlers)
    st.header('Highest Percentage for picking 4 Plus wickets in an Inning(Min 30 innings)')
    st.title('')
    chart = alt.Chart(four_or_more_wkts).mark_bar().encode(y='Player', x='per_picking_4+wkts', color='Country'). \
        properties(height=300, width=700)

    a1 = four_or_more_wkts.plot.barh()
    st.altair_chart(chart)

    # --------------------------------------------------------------------------
    st.title('')
    st.title('')

    top_bowler = Helper.top_bowlers(bowlers)
    st.header('Bowling Averages Comparison')
    plot = px.line(data_frame=top_bowler, x='Player', y='Ave', color='Country', width=1150)
    st.plotly_chart(plot)


else:

    st.header('The Greats of the Game')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        i2 = Image.open('don.png')
        st.image(i2, caption='Sir Donald Bradman', width=250)

    with col2:
        i3 = Image.open('border.png')
        st.image(i3, caption='Allan Border', width=250)
    with col3:
        i4 = Image.open('hobbs.png')
        st.image(i4, width=250, caption='Jack Hobbs')
    with col4:
        i5 = Image.open('hutton.png')
        st.image(i5, width=240, caption='Len Hutton')

    st.header('Runs Scored and Batting Averages of Both Countries')
    st.title('')
    col1, col2, col3, col4 = st.columns(4)
    runs_scored = Helper.runs(batters)
    innings_played = Helper.innings(batters)

    with col2:
        aus_batting_average = round((runs_scored['Runs'][0] / innings_played['Inns'][0]), 2)
        st.title('')
        st.title('')
        st.header(aus_batting_average)

    with col1:
        a = runs_scored['Runs'][0]
        st.header('Australia')
        st.header(a)

    with col3:
        e1 = runs_scored['Runs'][1]
        st.header('England')
        st.header(e1)

    with col4:
        eng_batting_average = round((runs_scored['Runs'][1] / innings_played['Inns'][1]), 2)
        st.title('')
        st.title('')
        st.header(eng_batting_average)

    st.title('')
    st.title('')

    hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.header('Top 5 Innings in Ashes History')
    st.title('')
    top_inning = Helper.top_innings(batters)
    st.table(top_inning)

    st.title('')
    st.title('')
    st.header('Highest Run Getters in The Ashes History')

    highest_run_getters = batters.sort_values(ascending=False, by='Runs').head()

    plot = px.bar(data_frame=highest_run_getters, x='Runs', y='Player', color='Country', width=1000)
    st.plotly_chart(plot)
    st.title('')
    st.title('')

    st.header('Percentage of Fifty plus scores')
    st.title('')
    scorers = Helper.fifty_plus_scores(batters)
    chart = alt.Chart(scorers).mark_bar().encode(y='Player', x='50+ scores percentage', color='Country'). \
        properties(height=300, width=1000)

    a1 = scorers.plot.barh()
    st.altair_chart(chart)

    st.title('')
    st.title('')

    top_batter = Helper.top_batters(batters)
    st.header('Batting Averages Comparison')
    plot = px.line(data_frame=top_batter, x='Player', y='Ave', color='Country', width=1150)
    st.plotly_chart(plot)
