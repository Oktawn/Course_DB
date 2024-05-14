import { Button } from "./Button";

export function Header() {
    return (
        <header>
            <Button text={"Личный кабинет"} />
            <Button text={"Рассписание"} />
            <Button text={"Оценки"} />
            <Button text={"Задания"} />
            <Button text={"Выйти"} />
        </header>
    )
}