class Reader():
    def __init__(self):
        self.__data = open('../data/contests_info.csv')

    def get_total_regions_open(self):
        #Retorna a quantidade de concursos abertos por estado
        total = {
            'AC':[],'AL':[],'AM':[],'AP':[],'BA':[],'CE':[],'DF':[],'ES':[],'GO':[],'MA':[],'MG':[],'MS':[],'MT':[],'PA':[],'PB':[],'PE':[],'PI':[],'PR':[],'RJ':[],'RN':[],'RO':[],'RR':[],'RS':[],'SC':[],'SE':[],'SP':[],'TO':[]
        }
        for data in self.__data:
            for key in total:
                if key == data.split(';')[0] and data.split(';')[3] == 'Aberto':
                    total[key].append(data.split(';')[2])
        for key in total:
            total[key] = len(total[key])
        return total

    def get_total_regions_predicted(self):
        #Retorna a quantidade de concursos previstpr por estado
        total = {
            'AC':[],'AL':[],'AM':[],'AP':[],'BA':[],'CE':[],'DF':[],'ES':[],'GO':[],'MA':[],'MG':[],'MS':[],'MT':[],'PA':[],'PB':[],'PE':[],'PI':[],'PR':[],'RJ':[],'RN':[],'RO':[],'RR':[],'RS':[],'SC':[],'SE':[],'SP':[],'TO':[]
        }
        for data in self.__data:
            for key in total:
                if key == data.split(';')[0] and data.split(';')[3] == 'Previsto':
                    total[key].append(data.split(';')[2])
        for key in total:
            total[key] = len(total[key])
        return total

    def get_contest_total_predicted(self):
        #Retorna o nome de concursos previstos por estado
        contests = {
            'AC':[],'AL':[],'AM':[],'AP':[],'BA':[],'CE':[],'DF':[],'ES':[],'GO':[],'MA':[],'MG':[],'MS':[],'MT':[],'PA':[],'PB':[],'PE':[],'PI':[],'PR':[],'RJ':[],'RN':[],'RO':[],'RR':[],'RS':[],'SC':[],'SE':[],'SP':[],'TO':[]
        }
        for data in self.__data:
            for key in contests:
                if key == data.split(';')[0]:
                    if data.split(';')[3] == 'Previsto':
                        contests[key].append(data.split(';')[1])
        return contests
    
    def get_contest_total_open(self):
        #Retorna o nome de concursos abertos por estado
        contests = {
            'AC':[],'AL':[],'AM':[],'AP':[],'BA':[],'CE':[],'DF':[],'ES':[],'GO':[],'MA':[],'MG':[],'MS':[],'MT':[],'PA':[],'PB':[],'PE':[],'PI':[],'PR':[],'RJ':[],'RN':[],'RO':[],'RR':[],'RS':[],'SC':[],'SE':[],'SP':[],'TO':[]
        }
        for data in self.__data:
            for key in contests:
                if key == data.split(';')[0]:
                    if data.split(';')[3] == 'Aberto':
                        contests[key].append(data.split(';')[1])
        return contests
    
    def get_total_vacancies(self):
        #Retorna a quantidade de vagas por estado em concursos abertos
        contests = {
            'AC':[],'AL':[],'AM':[],'AP':[],'BA':[],'CE':[],'DF':[],'ES':[],'GO':[],'MA':[],'MG':[],'MS':[],'MT':[],'PA':[],'PB':[],'PE':[],'PI':[],'PR':[],'RJ':[],'RN':[],'RO':[],'RR':[],'RS':[],'SC':[],'SE':[],'SP':[],'TO':[]
        }
        for data in self.__data:
            for key in contests:
                if key == data.split(';')[0]:
                    if data.split(';')[2] != 'Várias' and data.split(';')[3] == 'Aberto':
                        contests[key].append(data.split(';')[2])
        return contests
    
    def number_of_contests_per_region_open(self):
        #Retorna a quantidade de vagas por região em concursos abertos
        regions = {
            'norte' : [], 'nordeste' : [], 'centro_oeste': [], 'sudeste' : [], 'sul' : []
        }
        var_norte = 0
        var_nordeste = 0
        var_centro_oeste = 0
        var_sudeste = 0
        var_sul = 0
        
        for data in self.__data:
            if (data.split(';')[0] == 'AC' or data.split(';')[0] == 'AP' or data.split(';')[0] == 'AM' or 
                data.split(';')[0] == 'PA' or data.split(';')[0] == 'RO' or data.split(';')[0] == 'RR' or 
                data.split(';')[0] == 'TO') and data.split(';')[3] == 'Aberto':
                var_norte += 1
            elif (data.split(';')[0] == 'AL' or data.split(';')[0] == 'BA' or data.split(';')[0] == 'CE' or 
                data.split(';')[0] == 'MA' or data.split(';')[0] == 'PB' or data.split(';')[0] == 'PE' or 
                data.split(';')[0] == 'PI' or data.split(';')[0] == 'RN' or data.split(';')[0] == 'SE') and data.split(';')[3] == 'Aberto':
                var_nordeste += 1
            elif (data.split(';')[0] == 'DF' or data.split(';')[0] == 'GO' or data.split(';')[0] == 'MT' or 
                data.split(';')[0] == 'MS') and data.split(';')[3] == 'Aberto':
                var_centro_oeste += 1
            elif (data.split(';')[0] == 'ES' or data.split(';')[0] == 'MG' or data.split(';')[0] == 'RJ' or 
                data.split(';')[0] == 'SP') and data.split(';')[3] == 'Aberto':
                var_sudeste += 1
            elif (data.split(';')[0] == 'PR' or data.split(';')[0] == 'RS' or data.split(';')[0] == 'SC') and data.split(';')[3] == 'Aberto':
                var_sul += 1

        for key in regions:
            if key == 'norte':
                regions[key].append(var_norte)
            elif key == 'nordeste':
                regions[key].append(var_nordeste)
            elif key == 'centro_oeste':
                regions[key].append(var_centro_oeste)
            elif key == 'sudeste':
                regions[key].append(var_sudeste)
            elif key == 'sul':
                regions[key].append(var_sul)

        return regions

    def number_of_contests_per_region_predicted(self):
        #Retorna a quantidade de vagas por região em concursos previstos
        regions = {
            'norte' : [], 'nordeste' : [], 'centro_oeste': [], 'sudeste' : [], 'sul' : []
        }
        var_norte = 0
        var_nordeste = 0
        var_centro_oeste = 0
        var_sudeste = 0
        var_sul = 0
        
        for data in self.__data:
            if (data.split(';')[0] == 'AC' or data.split(';')[0] == 'AP' or data.split(';')[0] == 'AM' or 
                data.split(';')[0] == 'PA' or data.split(';')[0] == 'RO' or data.split(';')[0] == 'RR' or 
                data.split(';')[0] == 'TO') and data.split(';')[3] == 'Previsto':
                var_norte += 1
            elif (data.split(';')[0] == 'AL' or data.split(';')[0] == 'BA' or data.split(';')[0] == 'CE' or 
                data.split(';')[0] == 'MA' or data.split(';')[0] == 'PB' or data.split(';')[0] == 'PE' or 
                data.split(';')[0] == 'PI' or data.split(';')[0] == 'RN' or data.split(';')[0] == 'SE') and data.split(';')[3] == 'Previsto':
                var_nordeste += 1
            elif (data.split(';')[0] == 'DF' or data.split(';')[0] == 'GO' or data.split(';')[0] == 'MT' or 
                data.split(';')[0] == 'MS') and data.split(';')[3] == 'Previsto':
                var_centro_oeste += 1
            elif (data.split(';')[0] == 'ES' or data.split(';')[0] == 'MG' or data.split(';')[0] == 'RJ' or 
                data.split(';')[0] == 'SP') and data.split(';')[3] == 'Previsto':
                var_sudeste += 1
            elif (data.split(';')[0] == 'PR' or data.split(';')[0] == 'RS' or data.split(';')[0] == 'SC') and data.split(';')[3] == 'Previsto':
                var_sul += 1

        for key in regions:
            if key == 'norte':
                regions[key].append(var_norte)
            elif key == 'nordeste':
                regions[key].append(var_nordeste)
            elif key == 'centro_oeste':
                regions[key].append(var_centro_oeste)
            elif key == 'sudeste':
                regions[key].append(var_sudeste)
            elif key == 'sul':
                regions[key].append(var_sul)

        return regions