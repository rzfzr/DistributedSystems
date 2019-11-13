var net = require("net");

class Node {
    constructor(net, host, port, socketCallback) {
        this._net = net;
        this._host = host;
        this._port = port;
        this._socketCallback = socketCallback;
    }

    get net() {
        return this._net;
    }

    set net(net) {
        this._net = net;
    }

    get host() {
        return this._host;
    }

    set host(host) {
        this._host = host;
    }

    get port() {
        return this._port;
    }

    set port(port) {
        this._port = port;
    }

    get socketCallback() {
        return this._socketCallback;
    }

    set socketCallback(socketCallback) {
        return socketCallback;
    }

    get server() {
        return this._server;
    }

    set server(server) {
        this._server = server;
    }

    createServer() {
        this.server = this.net.createServer(this.socketCallback);
    }

    openServer() {
        this.server.listen(this.port, this.host);
    }

    get client() {
        return this._client;
    }

    set client(client) {
        this._client = client;
    }

    get remoteHost() {
        return this._remoteHost;
    }

    set remoteHost(remoteHost) {
        this._remoteHost = remoteHost;
    }

    get remoteSocketCallback() {
        return this._remoteSocketCallback;
    }

    set remoteHostSocketCallback(remoteSocketCallback) {
        this._remoteSocketCallback = remoteSocketCallback;
    }

    createClient() {
        this.client = this.net.createConnection(this.remotePort, this.remoteHost,
            this.remoteSocketCallback);
    }
}

function commandHandler(command) {
    var cmdString = command.toString();
    console.log(cmdString);
    var cmdJSON = JSON.parse(cmdString);
    node.remoteHost = cmdJSON.host;
    node.remotePort = cmdJSON.port;
    node.createClient();
    node.client.write("FUCK!");
}


// {"host": "127.0.0.1", "port": 8080}



function socketCallback(socket) {
    socket.write("hello\n");
    socket.on("data", commandHandler);
    socket.pipe(socket);
}

var node = new Node(net,
    '127.0.0.1',
    9090,
    socketCallback
);

node.createServer();
node.openServer();