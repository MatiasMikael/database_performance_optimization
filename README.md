# Tietokannan optimointiprojekti

## Yleiskatsaus
Tämä projekti keskittyy PostgreSQL-tietokannan suorituskyvyn optimointiin ja analysointiin. Projektiin sisältyi testidatan luominen, kyselyiden suorituskyvyn analysointi, indeksointi ja tulosten vertailu ennen ja jälkeen optimoinnin. Tavoitteena oli ymmärtää indeksoinnin vaikutus tietokantakyselyiden tehokkuuteen.

## Käytetyt työkalut ja kirjastot
- **Python**: Pääohjelmointikieli.
- **PostgreSQL**: Tietokanta, jossa optimointia suoritettiin.
- **SQLAlchemy**: Tietokantayhteyksien ja SQL-kyselyiden hallintaan.
- **dotenv**: Ympäristömuuttujien käsittelyyn.
- **psycopg2**: PostgreSQL-tietokantayhteyksiin.
- **Logging**: Lokitietojen tallentamiseen.
- **ChatGPT**: Projektin suunnitteluun ja toteutukseen.

## Projektin eteneminen

1. **Alustava suunnittelu**
   - Projektin tavoitteena oli testata indeksoinnin vaikutusta kyselyjen suorituskykyyn.
   - Projektirakenne määriteltiin kansiorakenteen ja skriptien avulla.

2. **Testidatan luonti**
   - Luotiin 1 000 käyttäjää, 200 tuotetta ja 10 000 tilausta.
   - Käytettiin Python-skriptiä nimeltä `generate_data.py` datan lisäämiseen tietokantaan.

3. **Kyselyiden suorituskykyanalyysi**
   - Analysoitiin kyselyitä `EXPLAIN (ANALYZE, BUFFERS)`-komennolla ennen optimointia.
   - Skripti `analyze_queries.py` tallensi tulokset lokitiedostoon.

4. **Indeksointi**
   - Lisättiin seuraavat indeksit suorituskyvyn parantamiseksi:
     - `orders.quantity`
     - `orders.user_id`
     - `orders.product_id`
   - Indeksointi toteutettiin skriptillä `create_indexes.py`.

5. **Optimoinnin jälkeinen analyysi**
   - Suoritettiin samat kyselyt ja analysoitiin, miten indeksointi vaikutti suorituskykyyn.
   - Tulokset osoittivat merkittäviä parannuksia suodatusehtoihin perustuvissa kyselyissä.

## Tulokset ja johtopäätökset
- **Indeksointi paransi merkittävästi suodatusehtoihin liittyvien kyselyiden suorituskykyä**.
  - Esimerkiksi kysely `SELECT * FROM orders WHERE quantity > 2` nopeutui huomattavasti indeksoinnin jälkeen.
- **Seq Scan -kyselyihin indeksit eivät vaikuttaneet**, koska nämä kyselyt lukevat koko taulun sisällön (esim. `SELECT * FROM users`).
- **Liittymät kyselyissä (JOIN)** hyötyivät osittain indeksoinnista, mutta vaikutus näkyy paremmin suuremmilla datamäärillä.
- Kaikki skriptit noudattivat **PEP 8** -ohjeistusta.

## Lisenssi
Tämä projekti on lisensoitu MIT-lisenssillä. Voit vapaasti käyttää, muokata ja jakaa tätä projektia ehtojen mukaisesti.
