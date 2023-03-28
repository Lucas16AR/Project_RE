import re
import time
import pandas as pd
import datetime
import constants as cs

class Analyzer:
    def operate_xlsx_file(self):
        file = pd.read_excel(cs.FULLPATH_XLSX)
        return file


#number1
    def search_sessions_by_user_id(self):
        df = self.operate_xlsx_file()
        user_id = input("Ingrese el ID del usuario: ")
        sessions = df.loc[df["Usuario"]==user_id, ["Usuario","Inicio de Conexion"]]
        if len(sessions) == 0:
            print(f"No se encontraron sesiones para el usuario {user_id}")
        else:
            print(sessions)
            sessions.to_excel(r"../files/Users_Sessions.xlsx", index=False)
            print(f"Se encontraron {len(sessions)} sesiones para el usuario {user_id}.")
            print(f"Las sesiones se han guardado en el archivo 'Users_Sessions.xlsx'.")


#number2
    def search_sessions_by_date_range_and_user_id(self):
        df = self.operate_xlsx_file()
        date_regex = re.compile(cs.DATETIME_REGEX)
        print(cs.DT_RANGE_MSG)
        time.sleep(2)
        print(cs.JUMP_LINE)
        date_1 = input(cs.DATETIME_INPUT_1)
        if not date_regex.fullmatch(date_1):
            print(cs.JUMP_LINE, cs.WRONG_DT_1)
            return
        print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
        date_2 = input(cs.DATETIME_INPUT_2)
        if not date_regex.fullmatch(date_2):
            print(cs.JUMP_LINE, cs.WRONG_DT_2)
            return
        print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
        user_id = input("Ingrese el ID del usuario: ")
        sessions = df.loc[(df["Usuario"]==user_id) & (df["Inicio de Conexion"]>=date_1) & (df["Inicio de Conexion"]<=date_2), ["Usuario","Inicio de Conexion"]]
        if len(sessions) == 0:
            print(f"No se encontraron sesiones para el usuario {user_id} en el rango de fechas especificado.")
        else:
            print(sessions)
            sessions.to_excel(r"../files/User_Sessions_Date.xlsx", index=False)
            print(f"Se encontraron {len(sessions)} sesiones para el usuario {user_id} en el rango de fechas especificado.")
            print(f"Las sesiones se han guardado en el archivo 'User_Sessions_Date.xlsx'.")


#number3
    def total_session_time(self):
        df = self.operate_xlsx_file()
        print(cs.JUMP_LINE)
        inp = input(cs.UN_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        if inp in df.values:
            df_loc = df.loc[:,["Usuario", "Session Time"]]
            df_loc = df_loc[df_loc["Usuario"].notnull()]
            user_df = df_loc[df_loc["Usuario"].str.contains(inp)]
            total_time_df = user_df['Session Time'].sum()
            print(cs.JUMP_LINE)
            total_time = str(datetime.timedelta(seconds=total_time_df))
            print("El tiempo total de este usuario es:", total_time)
        else:
            print(cs.JUMP_LINE, cs.USER_NOT_FOUND)
        time.sleep(0.1)


#number4
    def mac_user_devices1(self):
        print(cs.JUMP_LINE)
        inp = input(cs.MAC_USER_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file()
        
        if inp in df.values:
            df_loc = df.loc[:,["MAC Cliente", "Usuario"]]
            macs = df_loc[df_loc["MAC Cliente"].isin([inp])]
            mac_user = macs.groupby(['MAC Cliente', 'Usuario']).size().reset_index(name='Cantidad de Veces Utilizada')
            print(cs.JUMP_LINE)
            print(mac_user)
            mac_user.to_excel(cs.PATH_MAC_USER)
            print(cs.JUMP_LINE, cs.TO_EXCEL)
        else:
            print(cs.JUMP_LINE)
            print(cs.MAC_NOT_FOUND)
        time.sleep(0.1)





#number6
    def mac_ap_date1(self, specific_date = None):
        print(cs.JUMP_LINE)
        regex = re.compile(cs.DATETIME_REGEX)
        print(cs.JUMP_LINE, cs.DT_RANGE_MSG)
        time.sleep(2)
        print(cs.JUMP_LINE)
        date_1 = str(input(cs.DATETIME_INPUT_1))
        validation_date = regex.fullmatch(date_1)
        print(cs.JUMP_LINE)
        print(cs.VALIDATE_CHECKING)
        time.sleep(2)     
        if validation_date:
            print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
            date_2 = str(input(cs.DATETIME_INPUT_2))
            validation_date_2 = regex.fullmatch(date_2)
            print(cs.JUMP_LINE)
            print(cs.VALIDATE_CHECKING)
            time.sleep(2)
            if validation_date_2:
                print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
                mac_ap_input = str(input(cs.AP_INPUT))
                print(cs.JUMP_LINE,cs.SEARCHING_DATA, cs.JUMP_LINE)
                df = self.operate_xlsx_file()
                if mac_ap_input in df.values and date_1 < date_2:
                    df_loc = df.loc[:,["MAC AP", "Usuario", "Inicio de Conexion", "Fin de Conexio"]]
                    df_mac_date = df_loc[(df_loc["MAC AP"].isin([mac_ap_input])) & (df_loc["Inicio de Conexion"].between(date_1, date_2))]
                    print(df_mac_date)
                    df_mac_date.to_excel(cs.PATH_MAC_DT)
                    print(cs.JUMP_LINE, cs.TO_EXCEL)
                else:
                    print(cs.JUMP_LINE, cs.NO_MATCH)
            else:
                print(cs.JUMP_LINE, cs.WRONG_DT_2)
        else:
            print(cs.JUMP_LINE, cs.WRONG_DT_1)
        if validation_date is True:
            print(cs.JUMP_LINE)
            inp = input(cs.DATETIME_INPUT)
            validation_date = regex.fullmatch(inp)
            print(cs.JUMP_LINE)
            print(cs.VALIDATE_CHECKING)
            time.sleep(2)
            if validation_date:
                print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
                inp = inp.split("  ")
                inp.append("  ")
                inp.append("23:59:00")
                date_1 = inp[0] + inp[2] + inp[1]
                date_2 = inp[0] + inp[2] + inp[3]
                mac_ap_input = str(input(cs.AP_INPUT))
                print(cs.JUMP_LINE,cs.SEARCHING_DATA, cs.JUMP_LINE)
                df = self.operate_xlsx_file()
                if mac_ap_input in df.values and date_1 < date_2:
                    df_loc = df.loc[:,["MAC AP", "Usuario", "Inicio de Conexion", "Fin de Conexio"]]
                    df_mac_date = df_loc[(df_loc["MAC AP"].isin([mac_ap_input])) & (df_loc["Inicio de Conexion"].between(date_1, date_2))]
                    print(df_mac_date)
                    df_mac_date.to_excel(cs.PATH_MAC_DT)
                    print(cs.JUMP_LINE, cs.TO_EXCEL)
                else:
                    print(cs.JUMP_LINE, cs.NO_MATCH)
            else:
                print(cs.JUMP_LINE, cs.WRONG_DT_1)
        time.sleep(0.1)


#--------------------------------------------------------------------------------------------------------------------------
#number5
    def mac_user_devices2(self):
        print(cs.JUMP_LINE)
        inp = input(cs.MAC_USER_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file()
        if inp in df['MAC Cliente'].values:
            # df_loc = df.loc[:,["MAC Cliente", "Usuario", "Fecha"]]
            df_loc = df.loc[:,["MAC Cliente", "Usuario"]]
            macs = df_loc[df_loc["MAC Cliente"].isin([inp])]
            mac_user = macs.groupby(['MAC Cliente', 'Usuario']).size().reset_index(name='Cantidad de Veces Utilizada')
            mac_user['Dispositivo'] = inp
            # mac_user['Total Tiempo Conectado'] = macs.groupby(['MAC Cliente', 'Usuario'])['Fecha'].apply(lambda x: x.diff().sum()).dt.seconds
            # mac_user['Total Tiempo Conectado'] = macs.groupby(['MAC Cliente', 'Usuario']).apply(lambda x: x.diff().sum()).dt.seconds
            print(cs.JUMP_LINE)
            print(mac_user)
            mac_user.to_excel("mac_user_info.xlsx")
            print(cs.JUMP_LINE, cs.TO_EXCEL)
        else:
            print(cs.JUMP_LINE)
            print(cs.MAC_NOT_FOUND)
        time.sleep(0.1)


#number7