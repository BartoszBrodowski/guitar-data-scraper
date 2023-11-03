from neo4j import GraphDatabase

class Injector:
    def __init__(self, link):
        self.link = link
        self.driver = None

    def connect(self):
        try:
            print(f"Connecting to Neo4j database at {self.link}")
            self.driver = GraphDatabase.driver(self.link)
            print("Connected to the database successfully!")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            self.driver = None

    def inject_guitars(self, products):
        if self.driver is None:
            print("Database connection failed. Cannot inject data.")
            return
        query = 'CREATE (g:Guitar {id: $id, name: $name, manufacturer: $manufacturer, type: $type, price: $price, img: $img, url: $url})'
        for product in products:
            self.driver.execute_query(
                query,
                id=product.id,
                name=product.name,
                manufacturer=product.manufacturer,
                type=product.type,
                price=product.price,
                img=product.img,
                url=product.url
            )
        print('Data injected successfully!')