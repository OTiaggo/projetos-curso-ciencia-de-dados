from TSQL.run_query import TSQL


def main() -> None:
    print("==============================")
    print("Bem vindo ao interpretador T-SQL")
    print("Digite a consulta sql:")
    print("==============================")

    bd_connection = TSQL()

    while True:
        query = input("T-SQL> ")

        if query.lower() == "exit":
            break

        result = bd_connection.run_query(query)

        print("================================================")
        print("Resultado da query:")
        print(result)
        print("================================================")


if __name__ == "__main__":
    main()
