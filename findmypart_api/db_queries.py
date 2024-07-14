from decimal import Decimal

from settings import PAGE_SIZE


def search_part_sql(data, conn):
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

    query_map = {
        "model.name": f" AND model.name ILIKE '%{data.model_name}%'",
        "mark_name": f" AND mark.name ILIKE '%{data.mark_name}%'",
        "part_name": f" AND part.name ILIKE '%{data.part_name}%'",
        "price_gte": f" AND part.price >= {data.price_gte}",
        "price_lte": f" AND part.price <= {data.price_lte}",
        "mark_list": " AND mark.id = ANY('{" + ','.join(map(str, data.mark_list)) + "}')"
    }

    for key, value in data.__dict__.items():
        if key in query_map and value:
            query += query_map[key]

    if data.params:
        for param, value in data.params.items():
            if isinstance(value, int):
                query += f" AND part.json_data->>'{param}' ILIKE '{value}'"
            else:
                query += f" AND part.json_data->>'{param}' ILIKE '%{value}%'"

    cursor = conn.cursor()

    # Получение общего колличества и стоимости  найденных запчастей
    sql = f"""
        SELECT COUNT(*) count, COALESCE(SUM(parts.price), 0) sum
        FROM({query}) parts
    """
    cursor.execute(sql)
    row = cursor.fetchone()
    parts_price: Decimal = row['sum']
    parts_count: int = row['count']

    query += " ORDER BY part.id "
    query += f" LIMIT {PAGE_SIZE} OFFSET {offset}"

    cursor.execute(query)
    data = cursor.fetchall()

    return data, parts_count, parts_price
