from . import db
from .models import Protocol


def add_prot():
    protocols = {
        "dns": "DNS (ang. Domain Name System) - tłumaczy nazwy domen, takie jak np. cisco.com, na adresy IP. Protokół ten korzysta z portu 53.",
        "dhcpv4": "DHCPv4 (ang. Dynamic Host Configuration Protocol for IPv4) - serwer DHCPv4 dynamicznie przypisuje informacje adresowe IPv4 klientom DHCPv4 podczas uruchamiania i umożliwia ponowne wykorzystanie adresów, gdy nie są już potrzebne. DHCPv4 używa protokołu UDP i działa na portach 67 i 68.",
        "dhcpv6": "DHCPv6 (ang. Dynamic Host Configuration Protocol for IPv6) - DHCPv6 jest podobny do DHCPv4. Serwer DHCPv6 dynamicznie przypisuje informacje adresowe IPv6 klientom DHCPv6 podczas ich uruchamiania, działa na protach 546 i 547.",
        "slaac": "SLAAC (ang. Stateless Address Autoconfiguration) - metoda, która umożliwia urządzeniu uzyskanie informacji adresowych IPv6 bez użycia serwera DHCPv6.",
        'smtp': 'SMTP (ang. Simple Mail Transfer Protocol) - umożliwia klientom wysyłanie wiadomości e-mail do serwera poczty i umożliwia serwerom wysyłanie wiadomości e-mail do innych serwerów. Działa na porcie 25.',
        'pop3': 'POP3 (ang. Post Office Protocol - version 3) - umożliwia klientom pobieranie wiadomości e-mail z serwera poczty do lokalnej aplikacji poczty klienta. POP3 pracuje na porcie 110.',
        'imap': 'IMAP (ang. Internet Message Access Protocol) - umożliwia klientom dostęp do poczty e-mail przechowywanej na serwerze pocztowym, a także utrzymanie poczty na serwerze. Protokół ten działa na porcie 143.',
        'ftp': 'FTP (ang. File Transfer Protocol) - ustala reguły, za pomocą których użytkownik jednego hosta, może mieć dostęp i możliwość transmisji plików do i z innego hosta w sieci. Niezawodny, połączeniowy protokół wymiany plików, w którym stosuje się potwierdzanie. FTP korzysta z dwóch portów: portu sterującego (port 21) i portu danych (port 20).',
        'sftp': 'SFTP (ang. SSH File Transfer Protocol) - jako rozszerzenie protokołu Secure Shell (SSH), SFTP może być używany do ustanowienia bezpiecznej sesji transferu plików, w której transfer plików jest szyfrowany. SSH to metoda bezpiecznego zdalnego logowania, która jest zwykle używana do uzyskiwania dostępu do wiersza poleceń urządzenia. SFTP korzysta z portu 22.',
        'tftp': 'TFTP (ang. Trivial File Transfer Protocol) - prosty, bezpołączeniowy protokół przesyłania plików oparty o zasadę najlepszych starań i braku potwierdzeń w dostarczaniu plików. Mniej obciąża sieć niż protokół FTP. TFTP pracuje na porcie 69.',
        'http': 'HTTP (ang. Hypertext Transfer Protocol) - zestaw reguł wymiany tekstu, obrazów graficznych, dźwięku, wideo i innych plików multimedialnych w sieci WWW. HTTP działa na porcie 80.',
        'https': 'HTTPS (ang. Hypertext Transfer Protocol Secure) - bezpieczna forma HTTP, która szyfruje dane wymieniane w sieci www. Protokół ten działa na porcie 443.',
        'rest': 'REST (ang. Representational State Transfer) - usługa internetowa, która używa interfejsów programowania aplikacji (API) i żądań HTTP do tworzenia aplikacji internetowych.',
        'tcp': 'TCP (ang. Transmission Control Protocol) - umożliwia niezawodną komunikację między procesami działającymi na oddzielnych hostach i zapewnia niezawodne, potwierdzone transmisje, które weryfikują pomyślne dostarczenie.',
        'udp': 'UDP (ang. User Datagram Protocol) - pozwala procesowi uruchomionemu na jednym hoście na wysłanie pakietu do procesu uruchomionemu na innym hoście. Nie potwierdza udanej transmisji datagramu.',
        'ipv4': 'IPv4 (ang. Internet Protocol - version 4) - odbiera segmenty wiadomości z warstwy transportowej, umieszcza wiadomości w pakietach i adresuje pakiety w celu kompleksowego dostarczania przez sieć. Używa adresów 32-bitowych.', 'ipv6': 'IPv6 (ang. Internet Protocol - version 6) - podobny do IPv4, ale używa adresu 128-bitowego.',
        'nat': 'NAT (ang. Network Address Translation) - tłumaczy adresy IPv4 z sieci prywatnej na globalne, unikalne adresy IPv4.',
        'icmpv4': 'ICMPv4 (ang. Internet Control Message Protocol - version 4) - pozwala na przesłanie informacji zwrotnej z hosta docelowego do hosta źródłowego o błędach w dostarczaniu pakietów.',
        'icmpv6': 'ICMPv6 (ang. Internet Control Message Protocol - version 6) - podobna funkcjonalność do ICMPv4, ale jest używana dla pakietów IPv6.',
        'icmpv6nd': 'ICMPv6 ND (ang. Internet Control Message Protocol - version 6 Neighbor Discovery) - zawiera cztery komunikaty protokołu, które są używane do odwzorowania adresów i wykrywania zduplikowanych adresów.',
        'ospf': 'OSPF (ang. Open Shortest Path First) - protokół routingu stanu łącza, który używa hierarchicznej architektury opartej na obszarach. OSPF jest otwartym standardowym protokołem routingu wewnętrznego.',
        'eigrp': 'EIGRP (ang. Enhanced Interior Gateway Routing Protocol) - zastrzeżony protokół routingu firmy Cisco, który korzysta ze złożonej metryki opartej na przepustowości, opóźnieniu, obciążeniu i niezawodności.',
        'bgp': 'BGP (ang. Border Gateway Protocol) - otwarty protokół routingu zewnętrznej bramy używany między dostawcami usług internetowych (ISP). BGP używany jest również do wymiany informacji między ISP a ich największymi klientami prywatnymi.',
        'arp': 'ARP (ang. Address Resolution Protocol) - zapewnia dynamiczne odwzorowanie pomiędzy adresami IPv4 a adresami sprzętowymi.',
        'ethernet': 'Ethernet - określa reguły okablowania oraz standardy sygnalizacji w warstwie dostępu do sieci.',
        'wlan': 'WLAN (ang. Wireless Local Area Network) - określa zasady sygnalizacji bezprzewodowej w częstotliwościach radiowych 2,4 GHz i 5 GHz.'
    }
    for name, description in protocols.items():
        db.session.add(Protocol(
            name=name, description=description))
        db.session.commit()
