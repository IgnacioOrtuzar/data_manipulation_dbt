with all_data as (
select
    payment_id,
    order_id,
    payment_date,
    payment_method,
    payment_status,
    amount,
    row_number() over(partition by order_id
                    order by payment_date desc) as rn
from {{ ref('stg_payments') }}

),

metrics_data as (
    select
        order_id,
        count(*) as payment_attempts,

        sum(
            case 
                when payment_status = 'failed' then 1
                else 0
            end
        ) as failed_payment_count,

        sum(
            case 
                when payment_status = 'successful' then 1
                else 0
            end
        ) as successful_payment_count,

        sum(
            case 
                when payment_status = 'successful' then amount
                else 0
            end
        ) as successful_amount

    from all_data

    group by order_id
)


select 
    ad.order_id,
    ad.payment_date as last_payment_date,
    md.payment_attempts,
    md.failed_payment_count,
    md.successful_payment_count,
    case
        when md.successful_payment_count > 0 then true
        else false
    end as payment_successful,

    md.successful_amount
from
    all_data as ad
left join metrics_data as md
            on ad.order_id = md.order_id

where ad.rn = 1
