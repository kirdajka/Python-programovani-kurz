def convert_currencies (data):
    kurzy = {
        'PyCoin': 0.212,
        'CzechitaCoin': 0.457,
        # Polcoin je referenční měna, takže jeho hodnota vůči samotnému sobě je 1
        'Polcoin': 1.0
    }
    
    celkova_hodnota_v_polcoin = 0
    for mena, pocet in data.items():
        celkova_hodnota_v_polcoin += pocet * kurzy.get(mena, 0)
        
    return celkova_hodnota_v_polcoin

wallet = {"Polcoin": 100, "PyCoin": 13}
value = convert_currencies(wallet)
assert value == 102.756, f"add_two is {value}, but should be 102.756"

wallet = {"Polcoin": 100, "PyCoin": 13, "CzechitaCoin": 130}
value = convert_currencies(wallet)
assert value == 162.166, f"add_two is {value}, but should be 162.166!"