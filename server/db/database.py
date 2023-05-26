import click
import sqlite3
import os
import random


@click.group()
def cli():
    pass

# python database.py create-table
@cli.command()
def create_table():
    """Tạo bảng trong cơ sở dữ liệu SQLite từ file schema.sql."""
    try:
        click.echo('Bắt đầu tạo bảng.')
        # Lấy đường dẫn tới thư mục chứa script hiện tại
        current_dir = os.path.dirname(os.path.abspath(__file__))
        click.echo('current_dir: ' + current_dir)
        # Đọc nội dung của tệp schema.sql
        with open('schema.sql', 'r') as file:
            schema = file.read()

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect('database.sqlite')
        cursor = conn.cursor()

        # Thực thi câu lệnh SQL từ file schema.sql để tạo bảng
        cursor.executescript(schema)
        conn.commit()

        click.echo('Tạo bảng thành công!')
    except sqlite3.Error as e:
        click.echo('Lỗi khi tạo bảng: {}'.format(str(e)))
    finally:
        conn.close()


@cli.command()
@click.option('--count', default=10, help='Số lượng Asset cần thêm.')
def add_sample_asset(count):
    # Tạo kết nối tới cơ sở dữ liệu SQLite
    conn = sqlite3.connect('database.sqlite')

    # Tạo đối tượng cursor
    cursor = conn.cursor()
    # Dữ liệu mẫu cho các tài sản
    assets_data = []
    for i in range(count):
        name = f'Asset {i+1}'
        code = f'A{i+1}'
        price = random.uniform(1.0, 100.0)
        website = f'http://asset{i+1}.com'
        description = f'Description for Asset {i+1}'
        asset_type_id = 0
        assets_data.append((name, code, price, website, description,asset_type_id))

    # Chèn dữ liệu mẫu vào bảng "assets"
    cursor.executemany(
        'INSERT INTO asset (name, code, price, website, description,asset_type_id) VALUES (?, ?, ?, ?, ?, ?)', assets_data)

    # Lưu các thay đổi vào cơ sở dữ liệu
    conn.commit()

    # Đóng kết nối
    conn.close()

    click.echo('Tạo dữ liệu mẫu cho asset thành công!')


if __name__ == '__main__':
    cli()
