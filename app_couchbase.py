from couchbase.cluster import Cluster
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
import couchbase.options as opts
from datetime import timedelta
from couchbase.subdocument import decrement

def main():
    CONNECTION_STRING = "couchbase://localhost"
    USERNAME = "Administrador"
    PASSWORD = "123456"
    BUCKET_NAME = "trabalho_final"

    try:
        cluster = Cluster(CONNECTION_STRING, opts.ClusterOptions(PasswordAuthenticator(USERNAME, PASSWORD)))
        cluster.wait_until_ready(timeout=timedelta(seconds=10))
        bucket = cluster.bucket(BUCKET_NAME)
        # O objeto 'collection' é o que possui o método .mutate_in()
        collection = bucket.default_collection()
        print("✅ Conexão com Couchbase estabelecida!")

        produtos = {
            "prod:101": {"tipo": "produto", "nome": "Smartphone G-Phone 15 Pro", "preco": 7999.90, "estoque": 150, "ativo": True},
            "prod:205": {"tipo": "produto", "nome": "Notebook DevBook Air M4", "preco": 12500.00, "estoque": 80, "ativo": True}
        }

        print("\n📝 Inserindo/Resetando produtos no catálogo...")
        for key, doc in produtos.items():
            collection.upsert(key, doc)
        print("   - Produtos inseridos com sucesso.")

        print("\n===== DEMONSTRAÇÃO DA ATUALIZAÇÃO =====")

        notebook_antes = collection.get("prod:205").content_as[dict]
        print(f"📈 ANTES: O estoque do notebook é: {notebook_antes['estoque']}")

        print("\n🔄 Simulando uma venda e atualizando o estoque...")
        # --- CORREÇÃO AQUI ---
        # Chamamos .mutate_in() diretamente no objeto 'collection'
        # E passamos a operação 'decrement' que importamos
        collection.mutate_in("prod:205", [
            decrement("estoque", 5)
        ])
        print("   - Operação de atualização enviada.")

        notebook_depois = collection.get("prod:205").content_as[dict]
        print(f"📉 DEPOIS: O novo estoque do notebook é: {notebook_depois['estoque']}")
        print("==========================================")

    except CouchbaseException as e:
        print(f"❌ Erro de Couchbase: {e}")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()