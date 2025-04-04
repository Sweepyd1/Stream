<template>
    <div class="container">
        <div class="filters-container">
            <!-- Левая колонка -->
            <div class="filter-column">
                <div class="filter-group">
                    <h3>Тип</h3>
                    <label v-for="type in types" :key="type" class="filter-option">
                        <input type="radio" name="type" :value="type">
                        <span class="custom-radio"></span>
                        {{ type }}
                    </label>
                </div>

                <div class="filter-group">
                    <h3>Год выпуска</h3>
                    <div class="range-inputs">
                        <input type="number" placeholder="От" class="year-input">
                        <span class="dash">—</span>
                        <input type="number" placeholder="До" class="year-input">
                    </div>
                </div>

                <div class="filter-group">
                    <h3>Рейтинг</h3>
                    <select class="styled-select">
                        <option>Любой рейтинг</option>
                        <option>G — Детский</option>
                        <option>PG — Дети с родителями</option>
                        <option>R-17+</option>
                        <option>NC-17</option>
                    </select>
                </div>
            </div>

            <!-- Правая колонка -->
            <div class="filter-column">
                <div class="filter-group">
                    <h3>Жанры</h3>
                    <label v-for="genre in genres" :key="genre" class="filter-option">
                        <input type="checkbox" :value="genre">
                        <span class="custom-checkbox"></span>
                        {{ genre }}
                    </label>
                </div>

                <div class="filter-group">
                    <h3>Состояние</h3>
                    <label class="filter-option">
                        <input type="checkbox">
                        <span class="custom-checkbox"></span>
                        Только завершенные
                    </label>
                </div>
            </div>
        </div>

        <div class="apply_filter">
            <span>Применить фильтры</span>
        </div>
    </div>
</template>

<style scoped lang="scss">
.container {
   
    width: 700px;
    min-height: 45vh;
    max-height: 80vh;
    background-color: rgba(16, 14, 23, 0.95);
    border: 1px solid #8e60f4;
    box-shadow: 0 0 0 3px rgba(142, 96, 244, 0.2);
    border-radius: 8px;
    padding: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 20px;
    overflow-y: auto;
    
    

    .filters-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 25px;
    }

    .filter-column {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .filter-group {
        h3 {
            color: #C4B5FD;
            font-size: 14px;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
    }

    .filter-option {
        display: flex;
        align-items: center;
        gap: 10px;
        color: white;
        font-size: 14px;
        margin-bottom: 8px;
        cursor: pointer;
        transition: all 0.2s;

        &:hover {
            color: #C4B5FD;
        }

        input {
            display: none;

            &:checked + .custom-checkbox,
            &:checked + .custom-radio {
                background: #8e60f4;
                border-color: #8e60f4;

                &::after {
                    content: '';
                    display: block;
                    width: 6px;
                    height: 6px;
                    background: white;
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    border-radius: 1px;
                }
            }
        }

        .custom-checkbox {
            width: 16px;
            height: 16px;
            border: 2px solid #4A5568;
            border-radius: 4px;
            position: relative;
            transition: all 0.2s;
        }

        .custom-radio {
            width: 16px;
            height: 16px;
            border: 2px solid #4A5568;
            border-radius: 50%;
            position: relative;
        }
    }

    .styled-select {
        width: 100%;
        padding: 8px 12px;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #4A5568;
        border-radius: 6px;
        color: white;
        appearance: none;
        position: relative;
        background-image: url("data:image/svg+xml,%3Csvg width='12' height='8' viewBox='0 0 12 8' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1.5L6 6.5L11 1.5' stroke='%238e60f4' stroke-width='2'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: right 12px center;

        &:focus {
            outline: none;
            border-color: #8e60f4;
            box-shadow: 0 0 0 2px rgba(142, 96, 244, 0.2);
        }
    }

    .range-inputs {
        display: flex;
        align-items: center;
        gap: 8px;

        .year-input {
            width: 100%;
            padding: 8px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid #4A5568;
            border-radius: 6px;
            color: white;

            &::placeholder {
                color: #718096;
            }

            &:focus {
                outline: none;
                border-color: #8e60f4;
            }
        }

        .dash {
            color: #718096;
        }
    }

    .apply_filter {
        margin-top: auto;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 12px;
        width: 100%;
        background: linear-gradient(135deg, #8e60f4 0%, #6d28d9 100%);
        border-radius: 6px;
        border: none;
        color: white;
        transition: all 0.2s;

        &:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(142, 96, 244, 0.4);
        }

        span {
            font-size: 16px;
            font-weight: 500;
        }
    }
}
</style>

<script>
export default {
    data() {
        return {
            types: ['Сериал', 'Фильм', 'OVA', 'ONA'],
            genres: ['Экшен', 'Приключения', 'Комедия', 'Драма', 'Фантастика', 'Фэнтези', 'Ужасы', 'Романтика']
        }
    }
}
</script>