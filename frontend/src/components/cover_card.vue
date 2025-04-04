<template>

    <div class="card">
                        <div class="card-image">
                            <img src="@/assets/test_photo/test3.webp">
                     
                           
                        </div>
                        <h4 class="card-title">Атака Титанов</h4>
                        <div class="episode-info">Эпизод 12</div>
                    </div>
</template>
    
    
<style scoped lang="scss">
.card {
    flex: 0 0 200px;
    background: #1a1625;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s ease;
    
    

    &:hover {
        transform: translateY(-5px);
    }

    .card-image {
        position: relative;
        height: 280px;

        img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        .rating {
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            background: #8e60f4;
            opacity: 0.9;
            padding: 0.3rem 0.6rem;
            border-radius: 4px;
            font-size: 0.9rem;
            font-weight: 600;
            color: white;
        }
    }

    .card-title {
        font-size: 1rem;
        margin: 0.8rem;
        color: #fff;
    }

    .episode-info {
        font-size: 0.9rem;
        color: #a0aec0;
        margin: 0 0.8rem 0.8rem;
    }
}
</style>