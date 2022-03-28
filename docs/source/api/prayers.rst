The prayers module
******************

The ``Prayers`` class contains 13 methods, 12 of them return
different prayers, 1 method returns random prayers.

our_father
__________

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.our_father()
Our Father,
Who art in heaven,
hallowed be Thy name,
Thy kingdom come,
Thy will be done, on earth as it is in heaven.
Give us this day our daily bread,
and forgive us our trespasses
as we forgive those who trespass against us,
and lead us not into temptation,
but deliver us from evil.
Amem.

hail_mary
---------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.hail_mary()
Hail Mary, full of grace, the Lord is with thee.
Blessed art tthou amongst women,
and blessed is the fruit of thy womb, Jesus.
Holy Mary, Mother of God,
pray for us sinners,
now and at the hour of our death.
Amem.

glory_be
--------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.glory_be()
Glory be to the Father,
and to the Son,
and to the Holy Spirit,
as it was in the beginning,
is now, and ever shall be,
world without end.
Amem.

apostles_creed
--------------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.apostles_creed()
I believe in God,
the Father Almighty,
Creator of Heaven and earth;
and in Jesus Christ, His only Son, Our Lord,
Who was conceived by the Holy Spirit,
born of the Virgin Mary,
suffered under Pontius Pilate,
was crucified, died, and was buried.
He descended into Hell,
on the third day He arose again from the dead.
He ascended into Heaven,
and is seated at the right hand of God the Father Almighty;
from thence He shall come to judge
the living and the dead.
I believe in the Holy Spirit,
the holy Catholic Church,
the communion of saints,
the forgiveness of sins,
the resurrection of the body,
and the life everlasting.
Amem.

anima_christi
-------------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.anima_christi()
Soul of Christ, sanctify me,
Body of Christ, save me,
Blood of Christ, inebriate me,
Water from the side of Christ, wash me,
Passion of Christ, strengthen me,
O good Jesus, hear me.
Hide me within your wounds,
keep me close to  you,
defend me from the evil enemy,
call me at the hour of my death,
and bid me to come to you,
to praise you with your saints,
forever and ever.
Amem.

angelus
-------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.angelus()
The Angel of the Lord declared unto Mary.
And she conceived by the Holy Spirit.
Hail Mary, full of grace...
Behold the handmaid of the Lord.
Be it done unto me according to thy word.
Hail Mary, full of grace...
And the Word was made Flesh.
And dwelt among us.
Hail Mary, full of grace...
Pray for us, O Holy Mother of God,
that we may be made worthy of the promises of Christ.
Let us pray. Pour forth, we beseech thee,
O Lord, thy grace into our hearts, that we,
to whom the Incarnation of Christ, thy son,
was made known by the message of an angel,
may by his passion and cross be brought to the glory of his
resurrection, through the same Christ our Lord.
Amem.

saint_michael
-------------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.saint_michael()
Saint Michael the Archangel,
defend us in battle.
Be our protection against
the wickedness and snares of the devil.
May God rebuke him, we humbly pray,
and do thou, O Prince of the heavenly host,
by the power of God,
cast into hell Satan and all the evil spirits
who prowl throuhghout the world
seeking the ruin of souls.
Amem.

conversion_sinners
------------------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.conversion_sinners()
Lord Jesus Christ, most merciful Savior of the world,
we humbly beseech You, by Your most Sacred Heart,
that all the sheep who stray out of Your fold
may in one day be converted to You,
the Shepherd and Bishop of their souls, who lives and reigns
with God the Father in the unity of the Holy Spirit,
world without end.
Amem.

happy_death
-----------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.happy_death()
O my Lord and Savior,
support me in my last hour
by the strong arms of Thy sacraments
and the fragrance of thy consolations.
Let Thy absolving words be said over me,
and the holy oil sign and seal me;
and let Thine own body be my food and Thy blood my sprinkling;
and let Thy Mother Mary come to me,
and my angel whisper peace to me,
and Thy glorious saints and my own dear patrons smile on me,
that in and through them all I may die as I desire to live,
in Thy Church, in Thy faith, and in Thy love.
Amen.

come_holy_spirit
----------------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.come_holy_spirit()
Come Holy Spirit,
fill the hearts of your faithful
and kindle in them the fire of your love.
Send forth your Spirit and they shall be created.
And You shall renew the face of the earth.
O, God, who by the light of the Holy Spirit,
did instruct the hearts of the faithful,
grant that by the same Holy Spirit we may be truly wise
and ever enjoy His consolations,
Through Christ Our Lord,
Amem.

crux_sacra
----------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.crux_sacra()
Crux sacra sit mihi lux
Non draco sit mihi dux
Vade retro Sátana numquam suade mihi vana
Sunt mala quae libas ipse venena bibas

hail_holy_queen
---------------

>>> from pytholic.prayers import Prayers
>>> prayer = Prayers()
>>> prayer.hail_holy_queen()
Hail, holy Queen, Mother of mercy, hail, our life, our sweetness and our hope.
To thee do we cry, poor banished children of Eve:
to thee do we send up our sighs, mourning and weeping in this vale of tears.
Turn then, most gracious Advocate, thine eyes of mercy toward us, and after this our exile,
show unto us the blessed fruit of thy womb, Jesus, O merciful, O loving, O sweet Virgin Mary!
Amen.

random_prayer
-------------

This last method returns one of these prayers.