import datetime

from instapy import InstaPy

sessao = InstaPy(username='hoodtv.com.br', password='2571093014819Ll', headless_browser=False)
sessao.login()

sessao.follow_user_followers(usernames='primevideobr', amount=300)

#sessao.unfollow_users(amount=205, allFollowing=True, unfollow_after=0, sleep_delay=600)

sessao.end()