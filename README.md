## TLS
This scrip is an Exchange of Information via a TLS Server.

TLS stands for Transport Layer Security. It is a cryptographic protocol that adds encryption and authentication on top of TCP. Before the actual exchange of secured packets begins there is a TLS handshake phase during which the two communicating parties establish a TLS session. Messages exchanged during the handshake are secured with the asymmetric cryptography. Asymmetric cryptography relies on the certificate authorities and public/private key infrastructure. As the name says public key is available to everyone and it is distributed in the form of certificates that are signed by the certification authorities. Information encrypted with the public key can be decrypted only with the private key in the possession of the party to which a certificate with the corresponding public key is issued by the certification authority.

During the handshake phase, two communicating parties can authenticate to each other by exchanging the certificates. Furthermore, they also agree about a cipher and a symmetric secret key that will be used during the actual exchange of packets. Symmetric cryptography is used once the handshake is finished as it adds less computational overhead compared to the asymmetric cryptography. In the symmetric cryptography both parties use the same secret key.

## Author
[Locky](https://github.com/junlulocky)
