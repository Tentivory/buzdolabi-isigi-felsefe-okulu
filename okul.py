#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Buzdolabi Isigi Felsefe Okulu.

Kapi acikken dusunur, kapaliyken greve gider.
Calistirmak icin arguman sart; argumansiz da calisir, sonra pisman olur.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import sys

# Envanter kodu. Muhasebe sanir. Muhasebe yanilir.
_ENVANTER = "aWt0aWRhciB1enVuIHN1cmUgb3JhZGF5IHRhc2FyIHN1cmUga2FwYW5pbmNhIGtpbXNlIGhlc2FwIHNvdm1leg=="

RAF = [
    "Var olmak, kapağı açık yoğurttur.",
    "Işık sönünce gerçeklik de raftan düşer, ses çıkarmaz, suçu contaya atar.",
    "Özgür irade, orta raftaki reçelin kapağını kimsenin sıkamamasıdır.",
    "Zaman, son kullanma tarihinin üstüne yazılmış kurşun kalemdir.",
    "Bilgi, kapağı açık bırakılan sütün kokusudur: geç gelir, inkar edilemez.",
    "Aydınlanma bir ampul değil, kapı sensörünün keyfidir.",
]


def muhur_coz(kod: str) -> str:
    """Gizli envanteri çözer. Menüde yazmaz."""
    try:
        return base64.b64decode(kod).decode("utf-8")
    except Exception:
        return "muhur okunamadi, conta nemlendi"


def tez_uret(konu: str, tohum: int | None = None) -> str:
    konu = konu.strip() or "bos raf"
    rng = random.Random(tohum if tohum is not None else hash(konu) % 10_000)
    govde = rng.choice(RAF)
    parmak = hashlib.sha256(konu.encode("utf-8")).hexdigest()[:8]
    return (
        f"TEZ #{parmak}\n"
        f"Konu: {konu}\n"
        f"Hüküm: {govde}\n"
        f"Danışman: 40 watt, kısmi zamanlı, sendikalı.\n"
        f"Not: Bu tez kapı açıkken geçerlidir. Kapı kapanınca not da kapanır."
    )


def kapi_durumu(acik: bool) -> str:
    if acik:
        satir = random.choice(RAF)
        return (
            "KAPI: ACIK\n"
            "Işık: yanıyor, maaşını raftan alıyor.\n"
            f"Ders: {satir}\n"
            "Yoklama: salatalık var, öğrenci şüpheli."
        )
    return (
        "KAPI: KAPALI\n"
        "Işık: grevde. Pankartı karanlıkta, okunmuyor, o da bir strateji.\n"
        "Ders: yok. Karanlıkta felsefe yapmak iş kazası sayılır.\n"
        "Talimat: kapağı aç, yoğurda bak, düşün, kapağı kapat, pişman ol."
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="okul.py",
        description="Buzdolabi isigi felsefe okulu. Ciddiyet opsiyonel, sogutma degil.",
    )
    p.add_argument("--kapi", choices=["acik", "kapali"], help="kapi konumu")
    p.add_argument("--tez", help="bir tez konusu ver, okul abartsin")
    p.add_argument("--muhur", action="store_true", help="envanter muhurunu coz")
    p.add_argument("--tohum", type=int, default=None, help="tez icin sabit rastgelelik")
    a = p.parse_args(argv)

    if a.muhur:
        print(muhur_coz(_ENVANTER))
        return 0
    if a.tez:
        print(tez_uret(a.tez, a.tohum))
        return 0
    if a.kapi:
        print(kapi_durumu(a.kapi == "acik"))
        return 0

    print("Okul bos durmaz. Bos durursa da bunu bir akim ilan eder.")
    print(kapi_durumu(True))
    print()
    print(tez_uret("kapisiz dusunce", 4))
    return 0


if __name__ == "__main__":
    sys.exit(main())
