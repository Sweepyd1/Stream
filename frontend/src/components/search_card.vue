<template>
    <div class="some_anime">
            <div class="cover">
                <img src="@/assets/test_photo/avatar.jpg">

            </div>
            <div class="metadata">

                <div class="title">
                    <span>Какое то аниме</span>

                </div>
                <div class="description">
                    <span>Описание аниме</span>
                    
                </div>

            </div>

            <div class="rating">

            </div>
           
        </div>
        
</template>

<style scoped lang="scss">
 .some_anime{
        display: flex;
        width: 100%;
        min-height: 100px;
        padding: 16px;
        background: linear-gradient(145deg, rgba(24, 22, 37, 0.9) 0%, rgba(34, 30, 48, 0.9) 100%);
        border-radius: 8px;
        transition: all 0.3s ease;
        gap: 18px;
        position: relative;
        cursor: pointer;

        &:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(142, 96, 244, 0.3);
            background: linear-gradient(145deg, rgba(34, 30, 48, 0.95) 0%, rgba(44, 38, 62, 0.95) 100%);
        }

        .cover{
            width: 80px;
            height: 80px;
            flex-shrink: 0;
            border: 2px solid #8e60f4;
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.3s ease;

            img{
                width: 100%;
                height: 100%;
                object-fit: cover;
                transition: transform 0.3s ease;
            }

            &:hover img {
                transform: scale(1.05);
            }
        }

        .metadata {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 8px;
            padding-right: 20px;

            .title {
                span {
                    font-size: 1.4rem;
                    font-weight: 600;
                    background: linear-gradient(45deg, #a281ff, #d4b2ff);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    text-shadow: 0 2px 4px rgba(142, 96, 244, 0.2);
                }
            }

            .description {
                span {
                    color: #c0b3d8;
                    font-size: 0.95rem;
                    line-height: 1.4;
                    display: -webkit-box;
                    -webkit-line-clamp: 3;
                    -webkit-box-orient: vertical;
                    overflow: hidden;
                    text-overflow: ellipsis;
                }
            }
        }

        .rating {
            position: absolute;
            top: 12px;
            right: 12px;
            background: rgba(142, 96, 244, 0.15);
            padding: 6px 12px;
            border-radius: 20px;
            font-weight: 600;
            color: #d4b2ff;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 4px;

            &::before {
                content: '★';
                color: #ffd700;
                font-size: 1rem;
            }
        }
    }
</style>