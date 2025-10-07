import random

def version():
    vv = "0.6"
    return vv
import random
#=====zulfiQar()=========#
import random

def zulfiQar():
    # ====== Mobile Models (2023–2025 Fresh) ====== #
    moto = random.choice([
        "Moto G54 5G", "Motorola Edge 40", "Motorola Edge 50 Fusion",
        "Motorola Edge 50 Neo", "Motorola Edge 60 Pro", "Motorola Razr 50",
        "Moto G84", "Moto G Play 2024", "Moto G Power 5G", "Motorola Edge 2025"
    ])
    redmi = random.choice([
        "Redmi Note 12 Pro", "Redmi Note 12 Pro+ 5G", "Redmi Note 13 Pro",
        "Redmi Note 13 Pro+", "Redmi Note 14 Pro", "Redmi Note 14 Pro+",
        "Redmi Note 15 5G", "Redmi Note 15 Pro", "Redmi 14R", "Redmi K70"
    ])
    nokia = random.choice([
        "Nokia G42 5G", "Nokia XR21", "Nokia C32", "Nokia G310 5G",
        "Nokia C12 Pro", "Nokia C22", "Nokia C300", "Nokia G60 5G",
        "Nokia X30 5G", "Nokia XR40"
    ])
    samsung = random.choice([
        # ====== Samsung Galaxy S / A / M / Z Series (2023–2025) ====== #
        "Samsung Galaxy S21 FE", "Samsung Galaxy S22 Ultra", "Samsung Galaxy S23 Ultra",
        "Samsung Galaxy S24 Ultra", "Samsung Galaxy S25 Ultra", "Samsung Galaxy S25+",
        "Samsung Galaxy A15 5G", "Samsung Galaxy A25 5G", "Samsung Galaxy A55 5G",
        "Samsung Galaxy M14 5G", "Samsung Galaxy M44 5G", "Samsung Galaxy F54 5G",
        "Samsung Galaxy Z Fold6", "Samsung Galaxy Z Flip6", "Samsung Galaxy Tab S9"
    ])

    # ====== Android / Chrome / Facebook Versions ====== #
    version = random.choice(["8", "9", "10", "11", "12", "13"])
    chrome = f"{random.randint(120,138)}.0.{random.randint(6000,8000)}.{random.randint(50,200)}"
    fbav = f"{random.randint(400,510)}.0.0.{random.randint(10,99)}.{random.randint(100,999)}"
    fbbv = str(random.randint(300000000, 999999999))
    fbrv = str(random.randint(200000000, 999999999))
    fbnt = random.choice(["WIFI", "MOBILE"])
    fbca = random.choice([
        "arm64-v8a;", "armeabi-v7a;", "x86;", "x86_64;", "armv8l;"
    ])

    # ====== Random Carrier & Locale ====== #
    fbcr = random.choice([
        "Zong", "Jazz", "Telenor", "Ufone", "Airtel", "Jio", "Vodafone IN", "Grameenphone",
        "Robi", "Banglalink", "MTN", "Airtel Africa", "Glo", "Safaricom", "EE", "O2",
        "Vodafone UK", "Three UK", "BT Mobile", "Claro", "TIM", "Orange", "Movistar"
    ])
    fblc = random.choice([
        "en_GB", "en_US", "hi_IN", "ur_PK", "bn_BD", "id_ID", "es_ES", "fr_FR",
        "de_DE", "pt_BR", "ru_RU", "ar_SA", "th_TH", "vi_VN"
    ])

    # ====== Android UAs ====== #
    ua1 = (
        f"Mozilla/5.0 (Linux; Android {version}; {moto}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};"
        f"FBLC/{fblc};FBCR/{fbcr};FBMF/motorola;FBBD/motorola;"
        f"FBPN/com.facebook.katana;FBDV/{moto};FBSV/{version};"
        f"FBOP/1;FBCA/{fbca};FBNT/{fbnt}]"
    )

    ua2 = (
        f"Mozilla/5.0 (Linux; Android {version}; {redmi}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};"
        f"FBLC/{fblc};FBCR/{fbcr};FBMF/Xiaomi;FBBD/Redmi;"
        f"FBPN/com.facebook.katana;FBDV/{redmi};FBSV/{version};"
        f"FBOP/1;FBCA/{fbca};FBNT/{fbnt}]"
    )

    ua3 = (
        f"Mozilla/5.0 (Linux; Android {version}; {nokia}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};"
        f"FBLC/{fblc};FBCR/{fbcr};FBMF/Nokia;FBBD/Nokia;"
        f"FBPN/com.facebook.katana;FBDV/{nokia};FBSV/{version};"
        f"FBOP/1;FBCA/{fbca};FBNT/{fbnt}]"
    )

    ua4 = (
        f"Mozilla/5.0 (Linux; Android {version}; {samsung}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome} Mobile Safari/537.36 "
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};"
        f"FBLC/{fblc};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;"
        f"FBPN/com.facebook.katana;FBDV/{samsung};FBSV/{version};"
        f"FBOP/1;FBCA/{fbca};FBNT/{fbnt}]"
    )

    # ====== iOS UA ====== #
    ios_ver = f"{random.randint(15,18)}_{random.randint(0,9)}_{random.randint(0,9)}"
    ua5 = (
        f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) "
        f"AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 "
        f"[FBAN/FBIOS;FBAV/{fbav};FBBV/{fbbv};FBRV/{fbrv};"
        f"FBDV/iPhone{random.randint(10,16)},3;FBMD/iPhone;FBSN/iOS;"
        f"FBSV/{ios_ver.replace('_', '.')};FBCR/{fbcr};FBLC/{fblc};FBOP/80]"
    )

    # ====== Final UA Choice ====== #
    return random.choice([ua1, ua2, ua3, ua4, ua5])
    
import random

def ZAHOOR():
    samsung = random.choice([
        "SM-S918B", "SM-S916B", "SM-S925B", "SM-S919B", "SM-S918N",
        "SM-S916U", "SM-S918U", "SM-S916U1", "SM-S901B", "SM-S906B",
        "SM-E166P", "SM-E366B", "SM-F946B", "SM-F946U", "SM-F936B",
        "SM-A156U", "SM-A256U", "SM-A346U", "SM-M146B", "SM-M556B"
    ])
    moto = random.choice([
        "Moto G54 5G", "Motorola Edge 40", "Motorola Edge 50 Fusion",
        "Motorola Edge 50 Neo", "Motorola Edge 60 Pro", "Motorola Razr 50",
        "Moto G84", "Moto G Play 2024", "Moto G Power 5G", "Motorola Edge 2025"
    ])
    android_ver = random.choice(["13", "14", "15"])
    prefix = random.choice(["AP", "RP", "SP", "CP"])
    yymmdd = f"{random.randint(22,24):02d}{random.randint(1,12):02d}{random.randint(1,28):02d}"
    patch = f"{random.randint(1,999):03d}"
    sub = random.choice(["A1","A2","B1","B2","C1"])
    build = f"{prefix}{random.randint(1,9)}A.{yymmdd}.{patch}.{sub}"
    chrome_major = random.randint(120,138)
    chrome = f"{chrome_major}.0.{random.randint(7000,8200)}.{random.randint(1,999)}"
    fbav = f"{random.randint(520,540)}.0.0.{random.randint(10,99)}.{random.randint(10,99)}"
    fbcr = random.choice(["Zong","Jazz","Telenor","Ufone","Jio","Vodafone"])
    fblc = random.choice(["en_GB","en_US","ur_PK","hi_IN","es_ES"])
    ua1 = (
        f"Mozilla/5.0 (Linux; Android {android_ver}; {samsung} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 "
        f"[FB_IAB/FB4A;FBAV/{fbav};IABMV/1;FBLC/{fblc};FBCR/{fbcr};]"
    )
    ua2 = (
        f"Mozilla/5.0 (Linux; Android {android_ver}; {moto} Build/{build}; wv) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome} Mobile Safari/537.36 "
        f"[FB_IAB/FB4A;FBAV/{fbav};IABMV/1;FBLC/{fblc};FBCR/{fbcr};]"
    )
    return random.choice([ua1, ua2])


    
#======SIM1()========#
import random

def SIM1():
    aa = zulfiQar()
    bb = ZAHOOR()
    return random.choice([aa, bb])