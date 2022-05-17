

def add (table: str, name: str, last_name: str) -> str:
    text = f"""
            INSERT INTO {table}(First_Name, Last_Name)
            VALUES ('{name}', '{last_name}') 
            returning (First_Name, Last_Name);
            """
    return text
def edit (table: str, edname: str,edlast_name: str,edid: str)-> str:
        text = f"""
                UPDATE {table}
                SET first_name = '{edname}',last_name = '{edlast_name}' 
                WHERE id='{edid}' 
                returning *;
                """
        return text
        
def delete(table: str, did: str)-> str:
        text = f"""
                DELETE FROM {table}
                WHERE id ='{did}'
                returning*;
                """
        return text

