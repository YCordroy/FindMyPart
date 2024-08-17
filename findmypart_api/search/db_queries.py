from decimal import Decimal

PAGE_SIZE = 10


async def search_part_sql(data, conn):
    offset: int = (data.page - 1) * PAGE_SIZE
    query = """
        SELECT 
            part.*, 
            mark.id mark_id,
            mark.name mark_name,
            mark.producer_country_name, 
            model.id model_id, 
            model.name model_name
        FROM 
            partfinder_part part 
            JOIN partfinder_mark mark 
            ON part.mark_id = mark.id 
            JOIN partfinder_model  model 
            ON part.model_id = model.id 
        WHERE part.is_visible = TRUE
    """
    count = 1
    # Допустимые параметры запроса
    query_map = {
        "model_name": f" AND model.name ILIKE ",
        "mark_name": f" AND mark.name ILIKE ",
        "part_name": f" AND part.name ILIKE ",
        "price_gte": f" AND part.price >= ",
        "price_lte": f" AND part.price <= ",
        "mark_list": f" AND mark.id = ANY"
    }

    params = []
    for key, value in data.__dict__.items():
        if key in query_map and value and isinstance(value, str):
            query += query_map[key] + f'${count}'
            count += 1
            params.append(f"%{value}%")
        elif key in query_map and value and isinstance(value, float):
            query += query_map[key] + f'${count}'
            count += 1
            params.append(value)
        elif key in query_map and value and isinstance(value, list):
            query += query_map[key] + f'(${count})'
            count += 1
            params.append(value)
    # Обработка вложенных параметров
    if data.params:
        for param, value in data.params.items():
            if isinstance(value, int):
                if value in (True, False):
                    value = 'true' if value else 'false'
                query += f" AND part.json_data->>'{param}' = ${count}"
                value = str(value)
            else:
                query += f" AND part.json_data->>'{param}' ILIKE ${count}"
            count += 1
            params.append(value)
    # Получение общего колличества и стоимости  найденных запчастей
    sql = f"""
        SELECT COUNT(*) count, COALESCE(SUM(parts.price), 0) sum
        FROM({query}) parts
    """

    row = await conn.fetchrow(sql, *params)
    parts_price: Decimal = row['sum']
    parts_count: int = row['count']

    query += f" ORDER BY part.id LIMIT ${count} OFFSET ${count + 1}"
    params.extend([PAGE_SIZE, offset])
    data = await conn.fetch(query, *params)

    return data, parts_count, parts_price
