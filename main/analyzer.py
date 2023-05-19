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
        print(cs.JUMP_LINE, cs.LOADING_DATA)
        print(cs.JUMP_LINE)
        df = self.operate_xlsx_file()
        user_id = input(cs.UN_INP)
        sessions = df.loc[df["Usuario"]==user_id, ["Usuario","Inicio de Conexion"]]
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        time.sleep(1)
        print(cs.JUMP_LINE)
        if len(sessions) == 0:
            print(f"No se encontraron sesiones para el usuario {user_id}")
        else:
            print(sessions)
            sessions.to_excel(cs.USERS_SESSIONS, index=False)
            print(f"Se encontraron {len(sessions)} sesiones para el usuario {user_id}.")
            print(f"Las sesiones se han guardado en el archivo 'Users_Sessions_ID.xlsx'.")


#number2
    def search_sessions_by_date_range_and_user_id(self):
        print(cs.JUMP_LINE, cs.LOADING_DATA)
        print(cs.JUMP_LINE)
        df = self.operate_xlsx_file()
        date_regex = re.compile(cs.DATETIME_REGEX1)
        print(cs.DT_RANGE_MSG)
        time.sleep(1)
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
        user_id = input(cs.UN_INP)
        sessions = df.loc[(df["Usuario"]==user_id) & (df["Inicio de Conexion"]>=date_1) & (df["Inicio de Conexion"]<=date_2), ["Usuario","Inicio de Conexion"]]
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        time.sleep(1)
        print(cs.JUMP_LINE)
        if len(sessions) == 0:
            print(f"No se encontraron sesiones para el usuario {user_id} en el rango de fechas especificado.")
        else:
            print(cs.JUMP_LINE)
            time.sleep(1)
            print(sessions)
            print(cs.JUMP_LINE)
            time.sleep(1)
            sessions.to_excel(cs.USERS_SESSIONS, index=False)
            print(f"Se encontraron {len(sessions)} sesiones para el usuario {user_id} en el rango de fechas especificado.")
            print(f"Las sesiones se han guardado en el archivo 'User_Sessions_Date.xlsx'.")


#number3
    def total_session_time(self):
        print(cs.JUMP_LINE, cs.LOADING_DATA)
        print(cs.JUMP_LINE)
        time.sleep(0.5)
        df = self.operate_xlsx_file()
        inp = input(cs.UN_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        time.sleep(1)
        if inp in df.values:
            df_loc = df.loc[:,["Usuario", "Session Time"]]
            df_loc = df_loc[df_loc["Usuario"].notnull()]
            user_df = df_loc[df_loc["Usuario"].str.contains(inp)]
            total_time_df = user_df['Session Time'].sum()
            print(cs.JUMP_LINE)
            total_time = str(datetime.timedelta(seconds=total_time_df))
            print("El tiempo total de este usuario es:", total_time)
            print(cs.JUMP_LINE)
            time.sleep(1)
        else:
            print(cs.JUMP_LINE, cs.USER_NOT_FOUND)
        if total_time_df > 0:
            user_df.to_excel(cs.TOTAL_SESSION_TIME, index=False)
            print(f"El tiempo total del usuario se guardaron en el archivo 'Total_Session_Time.xlsx'")
        time.sleep(1)


#number4
    def mac_user_devices1(self):
        print(cs.JUMP_LINE, cs.LOADING_DATA)
        time.sleep(1)
        print(cs.JUMP_LINE)
        inp = input(cs.MAC_USER_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        time.sleep(1)
        df = self.operate_xlsx_file()
        if inp in df.values:
            df_loc = df.loc[:,["MAC Cliente", "Usuario"]]
            macs = df_loc[df_loc["MAC Cliente"].isin([inp])]
            mac_user = macs.groupby(['MAC Cliente', 'Usuario']).size().reset_index(name='Cantidad de Veces Utilizada')
            print(cs.JUMP_LINE)
            time.sleep(1)
            print(mac_user)
            print(cs.JUMP_LINE)
            mac_user.to_excel(cs.MAC_USER, index=False)
            time.sleep(1)
            print(f"La cantidad de veces que se conecto se guardara en el archivo 'Mac_User.xlsx'")
            print(cs.JUMP_LINE)
            time.sleep(1)
        else:
            print(cs.JUMP_LINE)
            print(cs.MAC_NOT_FOUND)
        time.sleep(1)


#number5
    def mac_user_devices2(self):
        print(cs.JUMP_LINE, cs.LOADING_DATA)
        time.sleep(1)
        print(cs.JUMP_LINE)
        inp = input(cs.MAC_USER_INP)
        print(cs.JUMP_LINE)
        print(cs.SEARCHING_DATA)
        df = self.operate_xlsx_file()
        df['MAC Cliente'].fillna(value='', inplace=True)
        macs = df[df['MAC Cliente'].str.contains(inp)]
        if not macs.empty:
            mac_user = macs.groupby(['MAC AP', 'Usuario']).size().reset_index(name='Cantidad de Veces Utilizada')
            mac_user['Dispositivo'] = inp
            print(cs.JUMP_LINE)
            print(mac_user)
            mac_user.to_excel(cs.MAC_USER_INFO, index=False)
            time.sleep(1)
            print(cs.JUMP_LINE)
            print(f"La cantidad de veces que se conecto se guardara en el archivo 'Mac_User_Info.xlsx'")
            print(cs.JUMP_LINE)
            time.sleep(1)
        else:
            print(cs.JUMP_LINE)
            print(cs.MAC_NOT_FOUND)
        time.sleep(0.1)


#number6
    def mac_ap_date1(self):
        regex = re.compile(cs.DATETIME_REGEX1)
        print(cs.JUMP_LINE, cs.LOADING_DATA)
        time.sleep(2)
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
                    time.sleep(2)
                    df_mac_date.to_excel(cs.MAC_AP_RANGE, index=False)
                    time.sleep(1)
                    print(cs.JUMP_LINE)
                    print(f"La cantidad de veces que se conecto con el rango de fechas se guardara en el archivo 'Mac_AP_Range.xlsx'")
                    print(cs.JUMP_LINE)
                    time.sleep(2)
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
                inp.append("23:59:59")
                date_1 = inp[0] + inp[2] + inp[1]
                date_2 = inp[0] + inp[2] + inp[3]
                mac_ap_input = str(input(cs.AP_INPUT))
                print(cs.JUMP_LINE,cs.SEARCHING_DATA, cs.JUMP_LINE)
                df = self.operate_xlsx_file()
                if mac_ap_input in df.values and date_1 < date_2:
                    df_loc = df.loc[:,["MAC AP", "Usuario", "Inicio de Conexion", "Fin de Conexio"]]
                    df_mac_date = df_loc[(df_loc["MAC AP"].isin([mac_ap_input])) & (df_loc["Inicio de Conexion"].between(date_1, date_2))]
                    print(df_mac_date)
                    time.sleep(2)
                    df_mac_date.to_excel(cs.MAC_AP_RANGE, index=False)
                    time.sleep(1)
                    print(cs.JUMP_LINE)
                    print(f"La cantidad de veces que se conecto con el rango de fechas se guardara en el archivo 'Mac_AP_Range.xlsx'")
                    print(cs.JUMP_LINE)
                    time.sleep(2)
                else:
                    print(cs.JUMP_LINE, cs.NO_MATCH)
            else:
                print(cs.JUMP_LINE, cs.WRONG_DT_1)
        time.sleep(0.1)


#number7
    def mac_ap_date2(self):
        print(cs.JUMP_LINE)
        regex = re.compile(cs.DATETIME_REGEX2)
        print(cs.JUMP_LINE, cs.LOADING_DATA)
        time.sleep(2)
        print(cs.JUMP_LINE)
        date_input = str(input(cs.DATETIME_INPUT_3))
        validation_date = regex.fullmatch(date_input)
        print(cs.JUMP_LINE)
        print(cs.VALIDATE_CHECKING)
        time.sleep(2)
        if validation_date:
            print(cs.JUMP_LINE, cs.VALIDATE_CORRECT, cs.JUMP_LINE)
            mac_ap_input = str(input(cs.AP_INPUT))
            print(cs.JUMP_LINE,cs.SEARCHING_DATA, cs.JUMP_LINE)
            df = self.operate_xlsx_file()
            df['Inicio de Conexion'] = pd.to_datetime(df['Inicio de Conexion'])
            if mac_ap_input in df.values:
                df_loc = df.loc[:,["MAC AP", "Usuario", "Inicio de Conexion", "Fin de Conexio"]]
                search_date = pd.to_datetime(date_input, format='%d/%m/%Y').normalize().date()
                df_mac_date = df_loc[(df_loc["MAC AP"].isin([mac_ap_input])) & (df_loc["Inicio de Conexion"].dt.date == search_date)]
                print(df_mac_date)
                time.sleep(2)
                df_mac_date.to_excel(cs.MAC_AP_DATE, index=False)
                time.sleep(1)
                print(cs.JUMP_LINE)
                print(f"La cantidad de veces que se conectó en una fecha específica se guardará en el archivo 'Mac_AP_Date.xlsx'")
                print(cs.JUMP_LINE)
                time.sleep(2)
            else:
                print(cs.JUMP_LINE, cs.NO_MATCH)
        else:
            print(cs.JUMP_LINE, cs.WRONG_DT_1)
        time.sleep(0.1)
    