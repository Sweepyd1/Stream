export class UserLogin {
    constructor(public email: string, public password: string) {}
}

export class NewUser{
    constructor(public email: string, public password: string, public username: string) {}
}