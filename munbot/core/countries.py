# coding=utf8
import enum
import re


class Regoinals(str, enum.Enum):
    a = '\N{REGIONAL INDICATOR SYMBOL LETTER A}'
    b = '\N{REGIONAL INDICATOR SYMBOL LETTER B}'
    c = '\N{REGIONAL INDICATOR SYMBOL LETTER C}'
    d = '\N{REGIONAL INDICATOR SYMBOL LETTER D}'
    e = '\N{REGIONAL INDICATOR SYMBOL LETTER E}'
    f = '\N{REGIONAL INDICATOR SYMBOL LETTER F}'
    g = '\N{REGIONAL INDICATOR SYMBOL LETTER G}'
    h = '\N{REGIONAL INDICATOR SYMBOL LETTER H}'
    i = '\N{REGIONAL INDICATOR SYMBOL LETTER I}'
    j = '\N{REGIONAL INDICATOR SYMBOL LETTER J}'
    k = '\N{REGIONAL INDICATOR SYMBOL LETTER K}'
    l = '\N{REGIONAL INDICATOR SYMBOL LETTER L}'
    m = '\N{REGIONAL INDICATOR SYMBOL LETTER M}'
    n = '\N{REGIONAL INDICATOR SYMBOL LETTER N}'
    o = '\N{REGIONAL INDICATOR SYMBOL LETTER O}'
    p = '\N{REGIONAL INDICATOR SYMBOL LETTER P}'
    q = '\N{REGIONAL INDICATOR SYMBOL LETTER Q}'
    r = '\N{REGIONAL INDICATOR SYMBOL LETTER R}'
    s = '\N{REGIONAL INDICATOR SYMBOL LETTER S}'
    t = '\N{REGIONAL INDICATOR SYMBOL LETTER T}'
    u = '\N{REGIONAL INDICATOR SYMBOL LETTER U}'
    v = '\N{REGIONAL INDICATOR SYMBOL LETTER V}'
    w = '\N{REGIONAL INDICATOR SYMBOL LETTER W}'
    x = '\N{REGIONAL INDICATOR SYMBOL LETTER X}'
    y = '\N{REGIONAL INDICATOR SYMBOL LETTER Y}'
    z = '\N{REGIONAL INDICATOR SYMBOL LETTER Z}'


class Countries(enum.Enum):
    @classmethod
    def get_country(cls, country_name: str):
        """
        Get a country by its name

        Args:
            country_name (str): The common name of the country
        
        Returns:
            Countries: The enum representation of the requested country, if one exists
        """
        return getattr(cls, ''.join(word.capitalize() for word in country_name.split(' ')))

    def get_flag(self) -> str:
        """
        Returns:
            str: The emoji flag for the country
        """
        return ''.join(getattr(Regoinals, letter) for letter in self.value.lower())

    def get_country_name(self) -> str:
        return re.sub(r'([a-z])([A-Z])', r'\1 \2', self.name, flags=re.UNICODE)

    Afghanistan = 'AF'
    ÅlandIslands = 'AX'
    Albania = 'AL'
    Algeria = 'DZ'
    AmericanSamoa = 'AS'
    Andorra = 'AD'
    Angola = 'AO'
    Anguilla = 'AI'
    Antarctica = 'AQ'
    AntiguaAndBarbuda = 'AG'
    Argentina = 'AR'
    Armenia = 'AM'
    Aruba = 'AW'
    Australia = 'AU'
    Austria = 'AT'
    Azerbaijan = 'AZ'
    Bahamas = 'BS'
    Bahrain = 'BH'
    Bangladesh = 'BD'
    Barbados = 'BB'
    Belarus = 'BY'
    Belgium = 'BE'
    Belize = 'BZ'
    Benin = 'BJ'
    Bermuda = 'BM'
    Bhutan = 'BT'
    Bolivia = 'BO'
    Bonaire = 'BQ'
    BosniaAndHerzegovina = 'BA'
    Botswana = 'BW'
    BouvetIsland = 'BV'
    Brazil = 'BR'
    BritishIndianOceanTerritory = 'IO'
    BritishVirginIslands = 'VG'
    BruneiDarussalam = 'BN'
    Bulgaria = 'BG'
    BurkinaFaso = 'BF'
    Burundi = 'BI'
    CaboVerde = 'CV'
    Cambodia = 'KH'
    Cameroon = 'CM'
    Canada = 'CA'
    CaymanIslands = 'KY'
    CentralAfricanRepublic = 'CF'
    Chad = 'TD'
    Chile = 'CL'
    China = 'CN'
    ChristmasIsland = 'CX'
    CocosIslands = 'CC'
    Colombia = 'CO'
    Comoros = 'KM'
    Congo = 'CG'
    CookIslands = 'CK'
    CostaRica = 'CR'
    Croatia = 'HR'
    Cuba = 'CU'
    Curaçao = 'CW'
    Cyprus = 'CY'
    Czechia = 'CZ'
    DRC = 'CD'
    Denmark = 'DK'
    Djibouti = 'DJ'
    Dominica = 'DM'
    DominicanRepublic = 'DO'
    Ecuador = 'EC'
    Egypt = 'EG'
    ElSalvador = 'SV'
    EquatorialGuinea = 'GQ'
    Eritrea = 'ER'
    Estonia = 'EE'
    Eswatini = 'SZ'
    Ethiopia = 'ET'
    FalklandIslands = 'FK'
    FaroeIslands = 'FO'
    Fiji = 'FJ'
    Finland = 'FI'
    France = 'FR'
    FrenchGuiana = 'GF'
    FrenchPolynesia = 'PF'
    FrenchSouthernTerritories = 'TF'
    Gabon = 'GA'
    Gambia = 'GM'
    Georgia = 'GE'
    Germany = 'DE'
    Ghana = 'GH'
    Gibraltar = 'GI'
    Greece = 'GR'
    Greenland = 'GL'
    Grenada = 'GD'
    Guadeloupe = 'GP'
    Guam = 'GU'
    Guatemala = 'GT'
    Guernsey = 'GG'
    Guinea = 'GN'
    GuineaBissau = 'GW'
    Guyana = 'GY'
    Haiti = 'HT'
    HeardIslandAndMcDonaldIslands = 'HM'
    HolySee = 'VA'
    Honduras = 'HN'
    HongKong = 'HK'
    Hungary = 'HU'
    Iceland = 'IS'
    India = 'IN'
    Indonesia = 'ID'
    Iran = 'IR'
    Iraq = 'IQ'
    Ireland = 'IE'
    IsleOfMan = 'IM'
    Israel = 'IL'
    Italy = 'IT'
    IvoryCoast = 'CI'
    Jamaica = 'JM'
    Japan = 'JP'
    Jersey = 'JE'
    Jordan = 'JO'
    Kazakhstan = 'KZ'
    Kenya = 'KE'
    Kiribati = 'KI'
    Kuwait = 'KW'
    Kyrgyzstan = 'KG'
    Laos = 'LA'
    Latvia = 'LV'
    Lebanon = 'LB'
    Lesotho = 'LS'
    Liberia = 'LR'
    Libya = 'LY'
    Liechtenstein = 'LI'
    Lithuania = 'LT'
    Luxembourg = 'LU'
    Macao = 'MO'
    Madagascar = 'MG'
    Malawi = 'MW'
    Malaysia = 'MY'
    Maldives = 'MV'
    Mali = 'ML'
    Malta = 'MT'
    MarshallIslands = 'MH'
    Martinique = 'MQ'
    Mauritania = 'MR'
    Mauritius = 'MU'
    Mayotte = 'YT'
    Mexico = 'MX'
    Micronesia = 'FM'
    Moldova = 'MD'
    Monaco = 'MC'
    Mongolia = 'MN'
    Montenegro = 'ME'
    Montserrat = 'MS'
    Morocco = 'MA'
    Mozambique = 'MZ'
    Myanmar = 'MM'
    Namibia = 'NA'
    Nauru = 'NR'
    Nepal = 'NP'
    Netherlands = 'NL'
    NewCaledonia = 'NC'
    NewZealand = 'NZ'
    Nicaragua = 'NI'
    Niger = 'NE'
    Nigeria = 'NG'
    Niue = 'NU'
    NorfolkIsland = 'NF'
    NorthKorea = 'KP'
    NorthMacedonia = 'MK'
    NorthernMarianaIslands = 'MP'
    Norway = 'NO'
    Oman = 'OM'
    Pakistan = 'PK'
    Palau = 'PW'
    Palestine = 'PS'
    Panama = 'PA'
    PapuaNewGuinea = 'PG'
    Paraguay = 'PY'
    Peru = 'PE'
    Philippines = 'PH'
    Pitcairn = 'PN'
    Poland = 'PL'
    Portugal = 'PT'
    PuertoRico = 'PR'
    Qatar = 'QA'
    Romania = 'RO'
    Russia = 'RU'
    Rwanda = 'RW'
    Réunion = 'RE'
    SaintBarthélemy = 'BL'
    SaintHelena = 'SH'
    SaintKittsAndNevis = 'KN'
    SaintLucia = 'LC'
    SaintMartin = 'MF'
    SaintPierreAndMiquelon = 'PM'
    SaintVincentAndTheGrenadines = 'VC'
    Samoa = 'WS'
    SanMarino = 'SM'
    SaoTomeAndPrincipe = 'ST'
    SaudiArabia = 'SA'
    Senegal = 'SN'
    Serbia = 'RS'
    Seychelles = 'SC'
    SierraLeone = 'SL'
    Singapore = 'SG'
    SintMaarten = 'SX'
    Slovakia = 'SK'
    Slovenia = 'SI'
    SolomonIslands = 'SB'
    Somalia = 'SO'
    SouthAfrica = 'ZA'
    SouthGeorgiaAndTheSouthSandwichIslands = 'GS'
    SouthKorea = 'KR'
    SouthSudan = 'SS'
    Spain = 'ES'
    SriLanka = 'LK'
    Sudan = 'SD'
    Suriname = 'SR'
    SvalbardAndJanMayen = 'SJ'
    Sweden = 'SE'
    Switzerland = 'CH'
    SyrianArabRepublic = 'SY'
    Taiwan = 'TW'
    Tajikistan = 'TJ'
    Tanzania = 'TZ'
    Thailand = 'TH'
    TimorLeste = 'TL'
    Togo = 'TG'
    Tokelau = 'TK'
    Tonga = 'TO'
    TrinidadAndTobago = 'TT'
    Tunisia = 'TN'
    Turkey = 'TR'
    Turkmenistan = 'TM'
    TurksAndCaicosIslands = 'TC'
    Tuvalu = 'TV'
    USVirginIslands = 'VI'
    USA = 'US'
    Uganda = 'UG'
    Ukraine = 'UA'
    UnitedArabEmirates = 'AE'
    UnitedKingdom = 'GB'
    UnitedStatesMinorOutlyingIslands = 'UM'
    Uruguay = 'UY'
    Uzbekistan = 'UZ'
    Vanuatu = 'VU'
    Venezuela = 'VE'
    VietNam = 'VN'
    WallisAndFutuna = 'WF'
    WesternSahara = 'EH'
    Yemen = 'YE'
    Zambia = 'ZM'
    Zimbabwe = 'ZW'
